import frappe
from healthcare.healthcare.doctype.lab_test.lab_test import (
    LabTest,
    load_result_format,
)


class CustomLabTest(LabTest):

    def validate(self):
        # Keep Healthcare compatible by assigning
        # the first selected template to the hidden field
        if self.custom_lab_test:
            self.template = self.custom_lab_test[0].lab_test

        super().validate()

    def after_insert(self):

        # Healthcare loads the first template
        super().after_insert()

        if not self.custom_lab_test:
            return

        # ---------------------------------------------------------
        # Tag all rows created from the first template
        # ---------------------------------------------------------
        first_template = frappe.get_doc(
            "Lab Test Template",
            self.custom_lab_test[0].lab_test
        )

        for row in self.normal_test_items:
            if not row.custom_test_group:
                row.custom_test_group = first_template.lab_test_name

        # ---------------------------------------------------------
        # Load remaining templates
        # ---------------------------------------------------------
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

            # -----------------------------------------------------
            # Tag only the newly added rows
            # -----------------------------------------------------
            for row in self.normal_test_items[before:]:
                row.custom_test_group = template.lab_test_name

        self.save(ignore_permissions=True)