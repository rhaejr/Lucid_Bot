import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("character.db")
c = conn.cursor()


table = """ CREATE TABLE IF NOT EXISTS characters (
                                        id integer PRIMARY KEY,
                                        character text NOT NULL,
                                        player integer,
                                        birth_date text,
                                        total_dap integer
                                    ); """
dap_table = """CREATE TABLE IF NOT EXISTS changes (
                                    id integer PRIMARY KEY,
                                    character_id integer NOT NULL,
                                    dap_change integer,
                                    date text NOT NULL,
                                    dm text NOT NULL,
                                    comment text,
                                    FOREIGN KEY (character_id) REFERENCES characters (id)
                                );"""


if conn is not None:
    try:
        c.execute(table)
        c.execute(dap_table)
    except Error as e:
        print(e)


client = commands.Bot(">")
TOKEN = "NzkyNTI2MzAzNjk2NzgxMzUz.X-e_ow.GTWQNhtQgzn_vdBSBmQgPLDSWGA"

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    n = ctx.author.display_name
    await ctx.send('Hi! {}'.format(n))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        member = await client.fetch_user(325991789611712513)
        channel = await member.create_dm()
        await channel.send(error)
        return
    raise error



client.run(TOKEN)
