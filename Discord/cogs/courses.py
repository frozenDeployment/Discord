from disnake.ext import commands
import disnake
from Discord.functions.main_func import ege_24_text_1, ege_24_text_2, ege_25_text_1, \
ege_25_text_2, ege_26_text_1, ege_26_text_2, ege_27_text_1, ege_27_text_2, \
krugosvetka_pro_text_1, krugosvetka_pro_text_2, c_university_text_1, \
c_university_text_2, trainer_2_text, trainer_7_text, trainer_8_text, trainer_15_text


class Courses(commands.Cog):
    '''Курсы'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.slash_command(name='егэ_24')
    async def ege_24(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс 24ого задания ЕГЭ по Информатике'''
        
        user = inter.author
        author = 'GTai — Всеотец'
        owner = await self.bot.fetch_user(172383544201445376)

        title, description, color = ege_24_text_1()
        embed_1 = disnake.Embed(title=title, description=description, color=color)
        embed_1.set_author(name=author)
        description = ege_24_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'
        
        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await inter.send(response)


    @commands.slash_command(name='егэ_25')
    async def ege_25(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс 25ого задания ЕГЭ по Информатике'''

        user = inter.author
        author = 'GTai — Всеотец'
        owner = await self.bot.fetch_user(172383544201445376)

        title, description, color = ege_25_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_25_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await inter.send(response)


    @commands.slash_command(name='егэ_26')
    async def ege_26(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс 26ого задания ЕГЭ по Информатике'''

        user = inter.author
        author = 'GTai — Всеотец'
        owner = await self.bot.fetch_user(172383544201445376)

        title, description, color = ege_26_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_26_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await inter.send(response)

    
    async def ege_27(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс 27ого задания ЕГЭ по Информатике'''

        user = inter.author
        author = 'GTai — Всеотец'
        owner = await self.bot.fetch_user(172383544201445376)

        title, description, color = ege_27_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = ege_27_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await inter.send(response)


    @commands.slash_command(name='кругосветка')
    async def krugosvetka_pro(self, inter: disnake.ApplicationCommandInteraction):
        '''Мастер-группа Кругосветка PRO ЕГЭ по Информатике'''

        user = inter.author
        author = 'GTai — Всеотец'
        owner = await self.bot.fetch_user(172383544201445376)

        title, description, color = krugosvetka_pro_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = krugosvetka_pro_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await inter.send(response)
    

    @commands.slash_command(name='си_вуз')
    async def c_university(self, inter: disnake.ApplicationCommandInteraction):
        '''Видео-курс Си для ВУЗа'''

        user = inter.author
        author = 'GTai — Всеотец'
        owner = await self.bot.fetch_user(172383544201445376)

        title, description, color = c_university_text_1()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)

        description = c_university_text_2(owner)
        embed_2 = disnake.Embed(description=description, color=color)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'

        await user.send(embed=embed_1)
        await user.send(embed=embed_2)
        await inter.send(response)


    @commands.slash_command(name='егэ_2')
    async def trainer_2(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс-тренажёр по 2ому заданию ЕГЭ Информатика'''

        user = inter.author
        author = 'GTai — Всеотец'

        title, description, color = trainer_2_text()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'

        await user.send(embed=embed_1)
        await inter.send(response)


    @commands.slash_command(name='егэ_8')
    async def trainer_8(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс-тренажёр по 8ому заданию ЕГЭ Информатика'''

        user = inter.author
        author = 'GTai — Всеотец'

        title, description, color = trainer_8_text()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'
        
        await user.send(embed=embed_1)
        await inter.send(response)


    async def trainer_7(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс-тренажёр по 7ому заданию ЕГЭ Информатика'''

        user = inter.author
        author = 'GTai — Всеотец'

        title, description, color = trainer_7_text()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'
        
        await user.send(embed=embed_1)
        await inter.send(response)


    async def trainer_15(self, inter: disnake.ApplicationCommandInteraction):
        '''Курс-тренажёр по 15ому заданию ЕГЭ Информатика'''

        user = inter.author
        author = 'GTai — Всеотец'

        title, description, color = trainer_15_text()
        embed_1 = disnake.Embed(
            title=title, description=description, color=color)
        embed_1.set_author(name=author)
        response = 'Полная информация была отправлена тебе в личные сообщения :)'

        await user.send(embed=embed_1)
        await inter.send(response)


def setup(bot: commands.Bot):
    bot.add_cog(Courses(bot))
