from disnake.ext import commands
import disnake
from functions import ege_24_text_1
from functions import ege_24_text_2
from functions import ege_25_text_1
from functions import ege_25_text_2
from functions import ege_26_text_1
from functions import ege_26_text_2
from functions import krugosvetka_pro_text_1
from functions import krugosvetka_pro_text_2
from functions import c_university_text_1
from functions import c_university_text_2
from functions import trainer_2_text
from functions import trainer_8_text


class Courses(commands.Cog):
    '''Курсы'''

    def __init__(self, client) -> None:
        self.client = client

    @commands.slash_command(name='егэ_24')
    async def ege_24(self, ctx):
        '''Курс 24ого задания ЕГЭ по Информатике'''
        
        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_24_text_1()
        embed_1 = disnake.Embed(title=title, description=description, color=color)
        embed_1.set_author(name=author)
        description = ege_24_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)
        
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.slash_command(name='егэ_25')
    async def ege_25(self, ctx):
        '''Курс 25ого задания ЕГЭ по Информатике'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_25_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_25_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.slash_command(name='егэ_26')
    async def ege_26(self, ctx):
        '''Курс 26ого задания ЕГЭ по Информатике'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = ege_26_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_26_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.slash_command(name='кругосветка')
    async def krugosvetka_pro(self, ctx):
        '''Мастер-группа Кругосветка PRO ЕГЭ по Информатике'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = krugosvetka_pro_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = krugosvetka_pro_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()
    

    @commands.slash_command(name='си_вуз')
    async def c_university(self, ctx):
        '''Видео-курс Си для ВУЗа'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = c_university_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = c_university_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await ctx.message.delete()


    @commands.slash_command(name='егэ_2')
    async def trainer_2(self, ctx):
        '''Курс-тренажёр по 2ому заданию ЕГЭ Информатика'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = trainer_2_text()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        await user.send(embed=embed_1)
        await ctx.message.delete()


    @commands.slash_command(name='егэ_8')
    async def trainer_8(self, ctx):
        '''Курс-тренажёр по 8ому заданию ЕГЭ Информатика'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = trainer_8_text()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        await user.send(embed=embed_1)
        await ctx.message.delete()


    @commands.command(name='егэ_15', aliases=['егэ15', 'ege15', 'тренажёр15',\
         'тренажер15', 'trainer15', 'trainer_15'])
    async def trainer_15(self, ctx):
        '''Курс-тренажёр по 15ому заданию ЕГЭ Информатика'''

        user = ctx.message.author
        author = 'GTai — Всеотец'
        owner = await self.client.fetch_user(172383544201445376)

        title, description, color = trainer_8_text()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        await user.send(embed=embed_1)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Courses(client))
