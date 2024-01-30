# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'libreria.categoria'
    _description = 'Modelo de Categoria'

    name = fields.Char(string='Nombre', required=True, help='Introduce el nombre de la categoria')
    descripcion = fields.Text(string='Descripcion')

class libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Modelo de Libro'

    name = fields.Char(string='Nombre', required=True)
    precio = fields.Float(string='Precio')
    ejemplares = fields.Integer(string='ejemplares')
    rotura_estoc = fields.Boolean(string='Rotura Estoc', compute='_compute_rotura_estoc')
    data = fields.Date(string='Data')
    segonama = fields.Boolean(string='Segonama')
    estado = fields.Selection([('bo','Bo'), ('regular', 'Regular'), ('dolent', 'Dolent')])

    @api.depends('ejemplares')
    def _compute_rotura_estoc(self):
        for record in self:
            record.rotura_estoc = record.ejemplares < 10

