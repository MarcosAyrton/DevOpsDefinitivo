"""CrearTablas

Revision ID: 8c83014885b0
Revises: 
Create Date: 2024-06-19 14:18:39.585324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c83014885b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('precio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('precio')
    op.drop_table('producto')
    op.drop_table('categoria')
    # ### end Alembic commands ###
