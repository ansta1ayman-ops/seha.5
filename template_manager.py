import os

from database import fetchall, execute, fetchone


TEMPLATES_DIR = "templates"


def get_templates():

    return fetchall(
        """
        SELECT id, name, file_path
        FROM templates
        ORDER BY id DESC
        """
    )



def delete_template(template_id):

    template = fetchone(
        """
        SELECT file_path
        FROM templates
        WHERE id=?
        """,
        (template_id,)
    )


    if template:

        try:

            if isinstance(template, dict):
                file_path = template["file_path"]
            else:
                file_path = template[0]


            if file_path and os.path.exists(file_path):
                os.remove(file_path)

        except Exception:
            pass


    execute(
        """
        DELETE FROM templates
        WHERE id=?
        """,
        (template_id,)
    )


    return True



def template_exists(name):

    result = fetchone(
        """
        SELECT id
        FROM templates
        WHERE name=?
        """,
        (name,)
    )

    return result is not None