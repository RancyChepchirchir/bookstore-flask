"""postgres

Revision ID: f9e56ed7c0bc
Revises: 
Create Date: 2018-12-13 21:12:39.402429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9e56ed7c0bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('real_name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_real_name'), 'author', ['real_name'], unique=False)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=2048), nullable=True),
    sa.Column('base_price', sa.Numeric(precision=11, scale=2), nullable=False),
    sa.Column('number_in_stock', sa.Integer(), nullable=False),
    sa.Column('is_featured', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_is_featured'), 'book', ['is_featured'], unique=False)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_table('category_discount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('discount_value', sa.Numeric(precision=11, scale=2), nullable=True),
    sa.Column('discount_percent', sa.Integer(), nullable=True),
    sa.Column('valid_from', sa.DateTime(), nullable=True),
    sa.Column('valid_until', sa.DateTime(), nullable=True),
    sa.Column('min_order_value', sa.Numeric(precision=11, scale=2), nullable=True),
    sa.Column('max_discount_amount', sa.Numeric(precision=11, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_discount_valid_from'), 'category_discount', ['valid_from'], unique=False)
    op.create_index(op.f('ix_category_discount_valid_until'), 'category_discount', ['valid_until'], unique=False)
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('surname', sa.String(length=128), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_email'), 'client', ['email'], unique=True)
    op.create_index(op.f('ix_client_phone_number'), 'client', ['phone_number'], unique=True)
    op.create_index(op.f('ix_client_surname'), 'client', ['surname'], unique=False)
    op.create_table('delivery_method',
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('genre',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('place', sa.String(length=64), nullable=False),
    sa.Column('street_name', sa.String(length=128), nullable=False),
    sa.Column('street_number', sa.String(length=8), nullable=False),
    sa.Column('zip_code', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_location_zip_code'), 'location', ['zip_code'], unique=False)
    op.create_index('location_index', 'location', ['place', 'street_name', 'street_number'], unique=False)
    op.create_table('payment_method',
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('publisher',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('tag',
    sa.Column('tag', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('tag')
    )
    op.create_table('author_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books_genres',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_name'], ['genre.name'], ),
    sa.PrimaryKeyConstraint('book_id', 'genre_name')
    )
    op.create_table('cover',
    sa.Column('path', sa.String(length=128), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('path')
    )
    op.create_index(op.f('ix_cover_book_id'), 'cover', ['book_id'], unique=False)
    op.create_table('discounts_genres',
    sa.Column('category_discount_id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['category_discount_id'], ['category_discount.id'], ),
    sa.ForeignKeyConstraint(['genre_name'], ['genre.name'], ),
    sa.PrimaryKeyConstraint('category_discount_id', 'genre_name')
    )
    op.create_table('opinion',
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=2048), nullable=True),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('payment_method_name', sa.String(length=64), nullable=True),
    sa.Column('delivery_method_name', sa.String(length=64), nullable=True),
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('payment_date', sa.DateTime(), nullable=False),
    sa.Column('total_price', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['delivery_method_name'], ['delivery_method.name'], ),
    sa.ForeignKeyConstraint(['payment_method_name'], ['payment_method.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_client_id'), 'order', ['client_id'], unique=False)
    op.create_index(op.f('ix_order_delivery_method_name'), 'order', ['delivery_method_name'], unique=False)
    op.create_index(op.f('ix_order_order_date'), 'order', ['order_date'], unique=False)
    op.create_index(op.f('ix_order_payment_date'), 'order', ['payment_date'], unique=False)
    op.create_index(op.f('ix_order_payment_id'), 'order', ['payment_id'], unique=False)
    op.create_index(op.f('ix_order_payment_method_name'), 'order', ['payment_method_name'], unique=False)
    op.create_table('product_pricing',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('valid_until', sa.DateTime(), nullable=False),
    sa.Column('valid_from', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Numeric(precision=11, scale=2), nullable=False),
    sa.Column('discount_unit', sa.String(length=32), nullable=False),
    sa.Column('min_order_value', sa.Numeric(precision=11, scale=2), nullable=False),
    sa.Column('max_discount_amount', sa.Numeric(precision=11, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'valid_until')
    )
    op.create_index(op.f('ix_product_pricing_valid_from'), 'product_pricing', ['valid_from'], unique=False)
    op.create_table('publishers_books',
    sa.Column('publisher_name', sa.String(length=128), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['publisher_name'], ['publisher.name'], ),
    sa.PrimaryKeyConstraint('publisher_name', 'book_id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=128), nullable=False),
    sa.Column('body', sa.String(length=4096), nullable=False),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.Column('upvotes', sa.Integer(), nullable=False),
    sa.Column('downvotes', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('taggings',
    sa.Column('tag', sa.String(length=64), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tag.tag'], ),
    sa.PrimaryKeyConstraint('tag', 'book_id')
    )
    op.create_table('authorships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('author_order', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['id'], ['author_name.id'], ),
    sa.PrimaryKeyConstraint('id', 'book_id')
    )
    op.create_table('item_ordered',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'book_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_ordered')
    op.drop_table('authorships')
    op.drop_table('taggings')
    op.drop_table('review')
    op.drop_table('publishers_books')
    op.drop_index(op.f('ix_product_pricing_valid_from'), table_name='product_pricing')
    op.drop_table('product_pricing')
    op.drop_index(op.f('ix_order_payment_method_name'), table_name='order')
    op.drop_index(op.f('ix_order_payment_id'), table_name='order')
    op.drop_index(op.f('ix_order_payment_date'), table_name='order')
    op.drop_index(op.f('ix_order_order_date'), table_name='order')
    op.drop_index(op.f('ix_order_delivery_method_name'), table_name='order')
    op.drop_index(op.f('ix_order_client_id'), table_name='order')
    op.drop_table('order')
    op.drop_table('opinion')
    op.drop_table('discounts_genres')
    op.drop_index(op.f('ix_cover_book_id'), table_name='cover')
    op.drop_table('cover')
    op.drop_table('books_genres')
    op.drop_table('author_name')
    op.drop_table('tag')
    op.drop_table('publisher')
    op.drop_table('payment_method')
    op.drop_index('location_index', table_name='location')
    op.drop_index(op.f('ix_location_zip_code'), table_name='location')
    op.drop_table('location')
    op.drop_table('genre')
    op.drop_table('delivery_method')
    op.drop_index(op.f('ix_client_surname'), table_name='client')
    op.drop_index(op.f('ix_client_phone_number'), table_name='client')
    op.drop_index(op.f('ix_client_email'), table_name='client')
    op.drop_table('client')
    op.drop_index(op.f('ix_category_discount_valid_until'), table_name='category_discount')
    op.drop_index(op.f('ix_category_discount_valid_from'), table_name='category_discount')
    op.drop_table('category_discount')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_is_featured'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_author_real_name'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
