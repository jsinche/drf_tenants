from django.db import migrations, connection
from django_tenants.utils import schema_context

def create_sp_for_tenants(apps, schema_editor):
    # Cambiar explícitamente al esquema actual (tenant)
    with schema_context(connection.schema_name):  # Asegura que se aplique al esquema correcto
        with connection.cursor() as cursor:
            cursor.execute("""
            CREATE OR REPLACE FUNCTION get_all_employees()
            RETURNS TABLE(id BIGINT, username VARCHAR, email VARCHAR) AS $$
            BEGIN
                -- Devuelve los resultados del SELECT
                RETURN QUERY SELECT users_user.id, users_user.username, users_user.email FROM users_user;
            END;
            $$ LANGUAGE plpgsql;
            """)

class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sp_for_tenants),
    ]