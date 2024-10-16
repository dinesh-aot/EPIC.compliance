"""complaint status column added


Revision ID: fa9e73a67290
Revises: 4d8298d2ac7c
Create Date: 2024-09-12 13:11:04.730140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa9e73a67290'
down_revision = '4d8298d2ac7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    complaintstatusenum = sa.Enum('OPEN', 'CLOSED', name='complaintstatusenum', create_type=True)
    complaintstatusenum.create(op.get_bind()) 
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.Enum('OPEN', 'CLOSED', name='complaintstatusenum'), nullable=True))
        # Set the default value for existing rows
    op.execute("UPDATE complaints SET status = 'OPEN' WHERE status IS NULL")

    # Now alter the column to make it non-nullable
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.alter_column('status', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.drop_column('status')
        batch_op.execute(sa.text("DROP TYPE IF EXISTS complaintstatusenum CASCADE"))

    # ### end Alembic commands ###
