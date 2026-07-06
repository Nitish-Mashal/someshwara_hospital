import re
import frappe

from healthcare.healthcare.doctype.lab_test.lab_test import (
    LabTest,
    load_result_format,
)


class CustomLabTest(LabTest):

    def validate(self):
        # -------------------------------------------------------
        # Keep Healthcare compatible
        # -------------------------------------------------------
        if self.custom_lab_test:
            self.template = self.custom_lab_test[0].lab_test

        # Run original Healthcare validation
        super().validate()

        # -------------------------------------------------------
        # Update reference range before saving
        # -------------------------------------------------------
        self.set_reference_range()

    def after_insert(self):
        # Let Healthcare create the first template rows
        super().after_insert()

        if not self.custom_lab_test:
            return

        # -------------------------------------------------------
        # Tag rows of first template
        # -------------------------------------------------------
        first_template = frappe.get_doc(
            "Lab Test Template",
            self.custom_lab_test[0].lab_test
        )

        for row in self.normal_test_items:
            if not row.custom_test_group:
                row.custom_test_group = first_template.lab_test_name

        # -------------------------------------------------------
        # Load remaining templates
        # -------------------------------------------------------
        for child in self.custom_lab_test[1:]:

            before = len(self.normal_test_items)

            template = frappe.get_doc(
                "Lab Test Template",
                child.lab_test
            )

            load_result_format(
                self,
                template,
                self.is_new(),
                self.template,
            )

            for row in self.normal_test_items[before:]:
                row.custom_test_group = template.lab_test_name

        # Update ranges after loading extra templates
        self.set_reference_range()

    def set_reference_range(self):

        if not self.patient:
            return

        age = frappe.db.get_value(
            "Patient",
            self.patient,
            "custom_age"
        )

        gender = (self.patient_sex or "").strip().lower()

        if age is None or not gender:
            return

        try:
            age = int(re.search(r"\d+", str(age)).group())
        except Exception:
            return

        for row in self.normal_test_items:

            if not row.normal_range:
                continue

            original = row.normal_range.strip()

            if "|" not in original:
                continue

            selected = None

            for line in original.splitlines():

                line = line.strip()

                if not line:
                    continue

                parts = [p.strip() for p in line.split("|")]

                if len(parts) != 4:
                    continue

                try:
                    from_age = int(parts[0])
                    to_age = int(parts[1])
                except ValueError:
                    continue

                range_gender = parts[2].lower()
                reference_range = parts[3]

                if (
                    from_age <= age <= to_age
                    and (
                        range_gender == "all"
                        or range_gender == gender
                    )
                ):
                    selected = reference_range
                    break

            if selected:
                row.normal_range = selected