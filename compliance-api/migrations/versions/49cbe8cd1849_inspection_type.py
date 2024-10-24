"""inspection type

Revision ID: 49cbe8cd1849
Revises: a1ef05f78002
Create Date: 2024-09-05 16:21:15.604467

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "49cbe8cd1849"
down_revision = "a1ef05f78002"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "inspection_type_options",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
            comment="The unique identifier of the option",
        ),
        sa.Column("name", sa.String(), nullable=True, comment="The name of the option"),
        sa.Column(
            "sort_order",
            sa.Integer(),
            nullable=True,
            comment="Order of priority. Mainly used order the options while listing",
        ),
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.Column("updated_date", sa.DateTime(), nullable=True),
        sa.Column("created_by", sa.String(length=100), nullable=False),
        sa.Column("updated_by", sa.String(length=100), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default="t", nullable=False),
        sa.Column("is_deleted", sa.Boolean(), server_default="f", nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "inspection_types",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
            comment="The unique identifier",
        ),
        sa.Column(
            "type_id",
            sa.Integer(),
            nullable=False,
            comment="The unique identifier of inspection type option",
        ),
        sa.Column(
            "inspection_id",
            sa.Integer(),
            nullable=False,
            comment="The unique identifier of the inspection",
        ),
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.Column("updated_date", sa.DateTime(), nullable=True),
        sa.Column("created_by", sa.String(length=100), nullable=False),
        sa.Column("updated_by", sa.String(length=100), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default="t", nullable=False),
        sa.Column("is_deleted", sa.Boolean(), server_default="f", nullable=False),
        sa.ForeignKeyConstraint(
            ["inspection_id"],
            ["inspections.id"],
            name="inspection_agencies_inspection_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["type_id"],
            ["inspection_type_options.id"],
            name="inspection_types_type_id_type_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("inspection_ir_types")
    op.drop_table("ir_type_options")
    with op.batch_alter_table(
        "inspection_unapproved_projects", schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column("type", sa.String(), nullable=True, comment="The type of project")
        )
        batch_op.add_column(
            sa.Column(
                "sub_type",
                sa.String(),
                nullable=True,
                comment="The sub type of the project",
            )
        )
    inspection_types = ["Field", "Administrative"]
    for idx, value in enumerate(inspection_types, start=1):
        op.execute(
            f"INSERT INTO inspection_type_options (id, sort_order, name, created_date, created_by) VALUES ({idx}, {idx}, '{value}', now() at time zone 'utc','system')"
        )
    topics = [
        "Acid rock drainage",
        "Access control",
        "Air quality",
        "Approvals",
        "Camp",
        "Caribou mitigation and monitoring plan",
        "Community engagement",
        "Consultation and development",
        "Compensation or relocation",
        "Conduct works in WEP without full approval",
        "Construction staging",
        "Dust management",
        "Environmental management plan",
        "Erosion and sediment control",
        "Equipment maintenance",
        "False or misleading",
        "Fish and fish habitat",
        "Hazardous waste management",
        "Heritage Resources",
        "Human-Wildlife Conflict Mitigation",
        "Hydrocarbon management",
        "Indigenous consultation",
        "Infestation mitigation",
        "Invasive plant management",
        "Monitoring",
        "Noise and vibration",
        "Non-hazardous waste management",
        "Open burning",
        "Preconstruction requirements",
        "Public engagement",
        "Records management",
        "Signage",
        "Site maintenance",
        "Site reclamation",
        "Social management plan",
        "Social and economic effects reporting",
        "Soil salvage",
        "Spill management",
        "Timber salvage",
        "Training",
        "Waste management",
        "Water quality",
        "Water management",
        "WEP - Phase 2 implementation",
        "WEP - Final Clean-up implementation",
        "Whitebark pine",
        "Wildlife mitigation",
        "Wildlife monitoring",
        "Wildlife attractant management",
    ]
    op.execute(sa.text("TRUNCATE topics RESTART IDENTITY"))
    for idx, value in enumerate(topics, start=1):
        op.execute(
            f"INSERT INTO topics (id, name, created_date, created_by) VALUES ({idx},'{value}', now() at time zone 'utc','system')"
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(
        "inspection_unapproved_projects", schema=None
    ) as batch_op:
        batch_op.drop_column("sub_type")
        batch_op.drop_column("type")

    op.create_table(
        "ir_type_options",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('ir_type_options_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
            comment="The unique identifier of the option",
        ),
        sa.Column(
            "name",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=True,
            comment="The name of the option",
        ),
        sa.Column(
            "sort_order",
            sa.INTEGER(),
            autoincrement=False,
            nullable=True,
            comment="Order of priority. Mainly used order the options while listing",
        ),
        sa.Column(
            "created_date", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "updated_date", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "created_by", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column(
            "updated_by", sa.VARCHAR(length=100), autoincrement=False, nullable=True
        ),
        sa.Column(
            "is_active",
            sa.BOOLEAN(),
            server_default=sa.text("true"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "is_deleted",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="ir_type_options_pkey"),
        sa.UniqueConstraint("name", name="ir_type_options_name_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "inspection_ir_types",
        sa.Column(
            "id",
            sa.INTEGER(),
            autoincrement=True,
            nullable=False,
            comment="The unique identifier",
        ),
        sa.Column(
            "ir_type_id",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
            comment="The unique identifier of ir type option",
        ),
        sa.Column(
            "inspection_id",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
            comment="The unique identifier of the inspection",
        ),
        sa.Column(
            "created_date", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "updated_date", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "created_by", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column(
            "updated_by", sa.VARCHAR(length=100), autoincrement=False, nullable=True
        ),
        sa.Column(
            "is_active",
            sa.BOOLEAN(),
            server_default=sa.text("true"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "is_deleted",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["inspection_id"],
            ["inspections.id"],
            name="inspection_agencies_inspection_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["ir_type_id"],
            ["ir_type_options.id"],
            name="inspection_ir_types_type_id_ir_type_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id", name="inspection_ir_types_pkey"),
    )
    op.drop_table("inspection_types")
    op.drop_table("inspection_type_options")
    # ### end Alembic commands ###
