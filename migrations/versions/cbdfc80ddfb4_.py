"""empty message

Revision ID: cbdfc80ddfb4
Revises: 
Create Date: 2018-11-25 23:57:50.585963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbdfc80ddfb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agencia',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('codigo_agencia', sa.String(length=5), nullable=True),
    sa.Column('direccion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inquilino',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=False),
    sa.Column('fecha_nacimiento', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=50), nullable=False),
    sa.Column('telefono', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('propietario',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=False),
    sa.Column('telefono', sa.String(length=10), nullable=False),
    sa.Column('direccion', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vivienda',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('propietario_id', sa.String(length=5), nullable=False),
    sa.Column('agencia_id', sa.String(length=5), nullable=False),
    sa.Column('numero', sa.String(length=5), nullable=True),
    sa.Column('cp', sa.String(length=5), nullable=True),
    sa.Column('poblacion', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['agencia_id'], ['agencia.id'], ),
    sa.ForeignKeyConstraint(['propietario_id'], ['propietario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('alquiler',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('inquilino_id', sa.String(length=5), nullable=False),
    sa.Column('vivienda_id', sa.String(length=5), nullable=False),
    sa.Column('fianza', sa.String(length=10), nullable=True),
    sa.Column('fecha_firma', sa.String(length=10), nullable=True),
    sa.Column('fecha_inicio', sa.String(length=10), nullable=True),
    sa.Column('fecha_fin', sa.String(length=10), nullable=True),
    sa.Column('importe_mensual', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['inquilino_id'], ['inquilino.id'], ),
    sa.ForeignKeyConstraint(['vivienda_id'], ['vivienda.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alquiler')
    op.drop_table('vivienda')
    op.drop_table('propietario')
    op.drop_table('inquilino')
    op.drop_table('agencia')
    # ### end Alembic commands ###
