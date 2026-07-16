from database import fetchall, execute


def add_field(
    template_id,
    field_name,
    page,
    x,
    y,
    font_size,
    font_name
):

    execute(
        """
        INSERT INTO fields
        (
            template_id,
            field_name,
            page,
            x,
            y,
            font_size,
            font_name
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            template_id,
            field_name,
            page,
            x,
            y,
            font_size,
            font_name
        )
    )



def get_fields(template_id):

    return fetchall(
        """
        SELECT *
        FROM fields
        WHERE template_id=?
        """,
        (template_id,)
    )



def delete_field(field_id):

    execute(
        """
        DELETE FROM fields
        WHERE id=?
        """,
        (field_id,)
    )


    return True