"""Initial

Revision ID: 09337ef4bce9
Revises: 
Create Date: 2021-08-23 16:04:48.366359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09337ef4bce9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('minimun', sa.Integer(), nullable=True),
    sa.Column('amount_per_package', sa.Integer(), nullable=True),
    sa.Column('max_availability', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_id'), ['id'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('telephone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_id'), ['id'], unique=False)

    op.create_table('puchase_order',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_user'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('puchase_order', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_puchase_order_id'), ['id'], unique=False)

    op.create_table('shopping_cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity_product', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='fk_product'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_user'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('shopping_cart', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_shopping_cart_id'), ['id'], unique=False)

    op.create_table('puchase_order_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('puchase_order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='fk_puchase_order_product'),
    sa.ForeignKeyConstraint(['puchase_order_id'], ['puchase_order.id'], name='fk_puchase_order'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_puchase_order_user'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('puchase_order_item', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_puchase_order_item_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puchase_order_item', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_puchase_order_item_id'))

    op.drop_table('puchase_order_item')
    with op.batch_alter_table('shopping_cart', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_shopping_cart_id'))

    op.drop_table('shopping_cart')
    with op.batch_alter_table('puchase_order', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_puchase_order_id'))

    op.drop_table('puchase_order')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_id'))

    op.drop_table('user')
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_id'))

    op.drop_table('product')
    # ### end Alembic commands ###
