#!/usr/bin/env python
# coding=utf8

from flask import current_app

from qwapp.plugin import Plugin, make_block_expression
import leagueoflegends

plugin = Plugin('League of Legends plugin', author = 'Marc Brinkmann', description = 'Allows the calculation of gold and item build orders', version = (0,1))

ITEM_BUILD_BLOCK_NAME = 'lol-item-build'

@plugin.on_signal('plugin-loaded')
def load_db(plugin, app):
	app.lol_db = leagueoflegends.ItemGraph.from_item_file(app.config['PLUGIN_LOL_DBFILE'])


@plugin.on_signal('special-loaded')
@plugin.on_signal('page-loaded')
def process(app, page):
	page.extract_blocks(ITEM_BUILD_BLOCK_NAME)
	for id, block in page.blocks[ITEM_BUILD_BLOCK_NAME]:
		try:
			build = leagueoflegends.Build.from_yaml(current_app.lol_db, block.strip())
			page.body = page.body.replace(id, '\n\n' + build.to_purchase_yaml())
		except Exception, e:
			page.body = page.body.replace(id, str(e))
