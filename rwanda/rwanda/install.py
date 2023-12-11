import frappe

from rwanda.utils import import_villages


def after_install():
    # Populate DB with Rwanda Administrative Levels
    import_villages()
