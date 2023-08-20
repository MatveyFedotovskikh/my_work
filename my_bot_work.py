def write_top(self,i,all_student)-> None:
            
            
            embed1 = disnake.Embed(
                title="Table top Rocket Coins",
                description='Rulse:\n🤛 -100 in top\n🤜 +100 in top\n👈 -10 in top\n👉 +10 in top\n✋ Delit Table',
                color=disnake.Colour.yellow(),
                #timestamp=datetime.datetime.now(),
            )

            embed1.set_author(
                name="All top coins",
                # url="https://disnake.dev/",
                icon_url="https://em-content.zobj.net/source/noto-emoji-animations/344/rocket_1f680.gif",
            )
            embed1.set_footer(
                text="Rocket Tech School",
                icon_url="https://em-content.zobj.net/source/noto-emoji-animations/344/rocket_1f680.gif",
            )
            
            embed1.set_thumbnail(url="https://em-content.zobj.net/source/noto-emoji-animations/344/rocket_1f680.gif")
            
            all_student_in_tab = all_student[i:i+10]
            all_student_in_tab = self.corect_list_student(all_student_in_tab)
            if i==0:
                embed1.add_field(name=f"🏆 # {all_student_in_tab[0][0]}", value=f'{all_student_in_tab[0][1]} |🚀{all_student_in_tab[0][2]}🚀| {all_student_in_tab[0][3]}', inline=False)
                embed1.add_field(name=f"🥈 # {all_student_in_tab[1][0]}", value=f'{all_student_in_tab[1][1]} |🚀{all_student_in_tab[1][2]}🚀| {all_student_in_tab[1][3]}', inline=False)
                embed1.add_field(name=f"🥉 # {all_student_in_tab[2][0]}", value=f'{all_student_in_tab[2][1]} |🚀{all_student_in_tab[2][2]}🚀| {all_student_in_tab[2][3]}', inline=False)
            else:
                embed1.add_field(name=f"Top {i+1} # {all_student_in_tab[0][0]}", value=f'{all_student_in_tab[0][1]} |🚀{all_student_in_tab[0][2]}🚀| {all_student_in_tab[0][3]}', inline=False)
                embed1.add_field(name=f"Top {i+2} # {all_student_in_tab[1][0]}", value=f'{all_student_in_tab[1][1]} |🚀{all_student_in_tab[1][2]}🚀| {all_student_in_tab[1][3]}', inline=False)
                embed1.add_field(name=f"Top {i+3} # {all_student_in_tab[2][0]}", value=f'{all_student_in_tab[2][1]} |🚀{all_student_in_tab[2][2]}🚀| {all_student_in_tab[2][3]}', inline=False)
            embed1.add_field(name=f"Top {i+4} # {all_student_in_tab[3][0]}", value=f'{all_student_in_tab[3][1]} |🚀{all_student_in_tab[3][2]}🚀| {all_student_in_tab[3][3]}', inline=False)
            embed1.add_field(name=f"Top {i+5} # {all_student_in_tab[4][0]}", value=f'{all_student_in_tab[4][1]} |🚀{all_student_in_tab[4][2]}🚀| {all_student_in_tab[4][3]}', inline=False)
            embed1.add_field(name=f"Top {i+6} # {all_student_in_tab[5][0]}", value=f'{all_student_in_tab[5][1]} |🚀{all_student_in_tab[5][2]}🚀| {all_student_in_tab[5][3]}', inline=False)
            embed1.add_field(name=f"Top {i+7} # {all_student_in_tab[6][0]}", value=f'{all_student_in_tab[6][1]} |🚀{all_student_in_tab[6][2]}🚀| {all_student_in_tab[6][3]}', inline=False)
            embed1.add_field(name=f"Top {i+8} # {all_student_in_tab[7][0]}", value=f'{all_student_in_tab[7][1]} |🚀{all_student_in_tab[7][2]}🚀| {all_student_in_tab[7][3]}', inline=False)
            embed1.add_field(name=f"Top {i+9} # {all_student_in_tab[8][0]}", value=f'{all_student_in_tab[8][1]} |🚀{all_student_in_tab[8][2]}🚀| {all_student_in_tab[8][3]}', inline=False)
            embed1.add_field(name=f"Top {i+10} # {all_student_in_tab[9][0]}", value=f'{all_student_in_tab[9][1]} |🚀{all_student_in_tab[9][2]}🚀| {all_student_in_tab[9][3]}', inline=False)
            return embed1

async def on_off_button(self) -> None:
            print(self.children)
            for items in self.children:
                if items.label == '👉'or items.label == '🤜':
                    if i==count_student-10:
                        items.disabled = True
                    else:
                        items.disabled = False
                if items.label == '👈' or items.label == '🤛':
                    if i==0:
                        items.disabled = True
                    else:
                        items.disabled = False
            
            await self.message.edit(view=self)
        
        @discord.ui.button(label = '🤛', style=discord.ButtonStyle.gray,disabled=True)
        async def SuperDown(self, interaction: discord.Interaction, button:discord.ui.Button) -> None:
            global i
            i-=100
            if i<0:
                i=0
            embed = self.write_top(i,self.all_student)
            self.foo = False
            await self.message1.edit(embed=embed)
            await interaction.response.edit_message(view=self)
            await self.on_off_button()

        @discord.ui.button(label = '👈', style=discord.ButtonStyle.gray,disabled=True)
        async def Down(self, interaction: discord.Interaction, button:discord.ui.Button) -> None:
            global i
            i-=10
            if i<0:
                i=0
            embed = self.write_top(i,self.all_student)
            self.foo = False
            await self.message1.edit(embed=embed)
            await interaction.response.edit_message(view=self)
            await self.on_off_button()

        @discord.ui.button(label = '👉', style=discord.ButtonStyle.gray)
        async def Up(self, interaction: discord.Interaction, button:discord.ui.Button) -> None:
            
            global i
            i+=10
            if i > count_student-10:
                i = count_student-10
            embed = self.write_top(i,self.all_student)
            self.foo = True
            await self.message1.edit(embed=embed)
            await interaction.response.edit_message(view=self)
            await self.on_off_button()
        
    

        @discord.ui.button(label = '🤜', style=discord.ButtonStyle.gray)
        async def SuperUp(self, interaction: discord.Interaction, button:discord.ui.Button) -> None:
            
            global i
            i+=100
            if i > count_student-10:
                i = count_student-10
            embed = self.write_top(i,self.all_student)
            self.foo = True
            await self.message1.edit(embed=embed)
            await interaction.response.edit_message(view=self)
            await self.on_off_button()
            
        
        @discord.ui.button(label = '✋Stop', style=discord.ButtonStyle.danger)
        async def Delete(self, interaction: discord.Interaction, button:discord.ui.Button) -> None:
            
            await self.message1.delete()
            await self.message.delete()
        

    class MyView(discord.ui.View):
        global ctx_flavor 

        async def on_timeout(self):
            for child in self.children:
                child.placeholder = '❌Время выбора истекло❌'
                child.disabled = True 
            await message_flavor.edit(content = f'❌<@{ctx_flavor.author.id}> Время выбора истекло❌',view=self)
            await asyncio.sleep(15)
            await message_flavor.delete()
            await message_img.delete()


        @discord.ui.select(
            placeholder = "Нажми на кнопку", 
            min_values = 1, 
            max_values = 1,
            disabled=False,
            options = [ 
                discord.SelectOption(
                    label="Компьютерная мышь проводная",
                    description="Компьютерная мышь проводная Цена: 2600 RC",
                    default = False,
                    emoji='🖱'
                ),
                discord.SelectOption(
                    label="Компьютерная мышь и Клавиатура",
                    description="Компьютерная мышь и Клавиатура Цена: 3000 RC",
                    default = False,
                    emoji='⌨️'
                ),
                discord.SelectOption(
                    label="Наушники",
                    description="Наушники Цена: 3000 RC",
                    default = False,
                    emoji='🎧'
                ),
                discord.SelectOption(
                    label="Roblox",
                    description="Gift-card на 800 Robux Цена: 2000 RC",
                    default = False,
                    emoji='💰'
                ),
                discord.SelectOption(
                    label="Netflix",
                    description="1 месяц подписки Цена: 2800 RC",
                    default = False,
                    emoji='📺'
                ),
                discord.SelectOption(
                    label="Spotify",
                    description="2 месяца подписки Цена: 2000 RC",
                    default = False,
                    emoji='🎵'
                ),
                discord.SelectOption(
                    label="Money",
                    description="10$ на карту твоих родителей Цена: 2000 RC",
                    default = False,
                    emoji='💳'
                ),
                discord.SelectOption(
                    label="Discord Intro",
                    description="1 месяц подписки Цена: 2000 RC",
                    default = False,
                    emoji='💎'
                ),
                discord.SelectOption(
                    label="Steam",
                    description="$10 на карту Steam Цена: 2000 RC",
                    default = False,
                    emoji='🎮'
                ),
                discord.SelectOption(
                    label="Групповой урок",
                    description="Групповой урок (80 минут) Цена: 1000 RC",
                    default = False,
                    emoji='🚀'
                ),
                discord.SelectOption(
                    label="Индивидуальный урок",
                    description="Групповой урок (50 минут) Цена: 1500 RC",
                    default = False,
                    emoji='🚀'
                )
            ]  
        )

        async def first_select_callback(self,select,interaction):
            global ctx_flavor
            for child in self.children:
                child.placeholder = f'{interaction.values[0]}✅'
                child.disabled = True 
            
            await select.response.edit_message(view=self)
            data = DataBase_client()
            if select.user.id != ctx_flavor.author.id:
                await message_flavor.edit(content = f'❌<@{select.user.id}> Данную команду, использовал другой человек, попробуй написать команду !rocket_shop и выбрать еще раз❌')
                return
        
            link_client = data.take_link_client(ctx_flavor.author.id,ctx_flavor.author) #data.take_link_client(ctx_flavor.author.id,ctx_flavor.author)
            if link_client is False:
                await message_flavor.edit(content = f'❌<@{ctx_flavor.author.id}> Я не нашел тебя в нашей Базе данных, Напиши пожалуйста <@697828423116259479>, он поможет тебе решить твою проблему')
                return
            
            score_user = data.take_score_bot(ctx_flavor.author)
            if score_user < rocket_shop_choice[interaction.values[0]]:
                await message_flavor.edit(content = f'❌<@{ctx_flavor.author.id}> Тебе не хватает {rocket_shop_choice[interaction.values[0]]-score_user} Rocket Coins ❌')
            else:
                if data.many_task_one_person(ctx_flavor.author):
                    await message_flavor.edit(content = f'❌<@{ctx_flavor.author.id}> У тебя уже есть покупка, которая ждет своего потверждения, если ты хочешь заново выбрать товары, то напиши команду !clear_shop ❌')
                else:
                    data.write_task(link_client,interaction.values[0],ctx_flavor.author.id,ctx_flavor.author)
                    await message_flavor.edit(content = (
                        f"Все прошло успешно ✅\n\n"
                        f"{ctx_flavor.author} ты выбрал {interaction.values[0]}\n" 
                        "В течении нескольких дней с тобой свяжутся администраторы нашей школы\n" 
                        "Для того чтобы отследить статус своего заказа, используй команду !my_shopping"))
            ctx_flavor = None
