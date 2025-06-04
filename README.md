--!!!ВНИМАНИЕ!!!--

	Рекомендуется прочитать всю инструкцию, здесь будет написаны все механики игры и подробный гайд по созданию своего персонажа
	Сначало будет написано по-английски затем будет перевод на русском

--!!!Attention!!!--

	It is recommended to read the entire instructions, all the mechanics of the game and a detailed guide for creating your character will be written here.
	First it will be written in English, then there will be a translation in Russian.

ENGLISH

	--Short Description--
	
		 This project is in the fighting game genre. 
		 Target audience: Children, teenagers, novice programmers
		 Inspired by the Mortal Kombat game series
		 The project was created so that users can compete in extreme battles with each other.
		 The project is also great for novice programmers because of the simple way to create your own characters. 
	
	--Management--
	
		--Player 1--
			w - jump
			s - squat
			d - kick
			a - block
	 		f - footboard
	 		r - block penetration
	 		t - activating rage
	 	--Player 2--
			up arrow - jump
			Down arrow - squat
			left arrow - kick
			right arrow - block
			L block - footboard
			k - block breakdown
			j - Activating rage
	
	--Mechanics--
	
		--Counter--
			Normal attacks can be evaded by swearing in or blocking
			normal attacks that deal the most damage
			Breaking through the block can only be avoided by swearing
			breaking through the block disables the block to the player and does some damage.
			The footboard can only be dodged by jumping
			. The footboard disables the player's squat.
			Rage multiplies all damage by 3
	 --Stats--
	 
		The stats of the characters show MAX health, name, armor, Damage multiplier, Rage multiplier
		 Armor performance: divides all damage received by the armor score with a 50-50 chance
		Rage Performance: The rage multiplier affects the rate of receiving and decreasing rage the higher the multiplier, the less rage goes away and is added faster
	
	
		When dodging any attacks other than a block, rage increases
	 	When you protect yourself from blows with a block, you get a health boost.
	
	--Create your own character--
		--NOTE-- if there are more than 8 characters, only the first 8 will be displayed
	
	 --Step 1--
		Draw animations for the character:
		--!!! WHEN DRAWING ANIMATIONS, MAKE ALL FRAMES AND ALL ANIMATIONS HAVE THE SAME AREA, 57 BY 61 PIXELS IS RECOMMENDED!!!-- otherwise the animation will twitch
	 	Please note that it is recommended to draw only as many frames as written below, otherwise you may make animations too fast.
	 	If something is not clear, you can look at the character frame files that have already been made.
	 		idle - no more than 13 frames
			kick 1 - no more than 3 frames
			kick 2 - no more than 3 frames
			squat - no more than 2 frames
			block - no more than 2 frames
			jump - no more than 5 frames
			block penetration - no more than 8 frames
			footboard - no more more than 13 frames
	 --NOTE-- When creating a new character, it is recommended to copy the existing character folder, rename it and see the animation structure and change it.
	 !!!THE NAMES OF THE FRAMES SHOULD BE NAMED STARTING FROM ZERO!!!
	---Step 2--
		Draw more pictures of the characters:
		the icon in the menu
		is the inscription of the win
	 	Don't be shy about looking at an example of how existing characters are created
	--- Step 3-
		The most difficult part is over
	 	Character Characteristics task:
		1.Open a text file heroes_data.txt in the assets/heroes folder
	 	2.The structure is given:
		{
	    	"Blue": {
	        	"name": "Tony",
	        	"HP": 220,
	        	"DEF": 3,
	        	"DMG": 4,
	        	"RAGE": 2,
	        	"BACKGROUND_C": [0, 128, 255]
	    		}, - после нового персонажа оставьте запятую
	    	"Example": {
	        	"name": "Write Name",
	        	"HP": Write MAX health,
	        	"DEF": Write Multiplier of defence,
	        	"DMG": Write Multiplier of damage,
	        	"RAGE": Write Multiplier of rage,
	        	"BACKGROUND_C": [255, 51, 51] - the background color of the card is Google RGB and substitute the numbers by selecting the color
	    		}
		{
	
	Just change what is instead of "Example" - the name of the folder with the character's files and where it says "Write" and the numbers as in the example 255,51,51
	That's it! The character is ready, enjoy the game, don't forget to save the text document after editing.
	
	If you liked it, add it to your favorites on github, I'll be glad! :)



РУССКИЙ

	--Краткое Описание--
	
		Данный проект в жанре файтинг. 
		Целевая аудитория: Дети, подростки, начинающие программисты
		Вдохновлено серией игр Mortal Kombat
		Проект создан, чтобы пользователи могли соревноваться в вируальных боях друг с другом.
		Также проект отлично подходит для начинающих программистов из-за простого способа создания своих персонажей  
	
	--Управление--
	
		--Игрок 1--
			w - прыжок
			s - присед
			d - удар
			a - блок
			f - подножка
			r - пробитие блока
			t - активирование ярости
		--Игрок 2--
			стрелка вверх - прыжок
			стрелка вниз - присед
			стрелка в лево - удар
			стрелка в право - блок
			l - подножка
			k - пробитие блока
			j - активирование ярости
	--Механики--
		--Контра--
			От обычных атак можно уклонятся в присяде либо блоком
				обычные атаки наносят больше всего урона
			От пробития блока можно уклонятся только в присяде
				пробитие блока отключает блок игроку и наносит немного урона
			От подножки можно уклонятся только прыжком
				подножка отключает присед игроку и наносит немного урона
			Ярость умножает весь урон на 3
		--Статистики--
			В статистиках персонажей написано МАКС здоровье, имя, броня, множитель урона,множитель ярости
				Работа брони: с шансом 50 на 50 делит весь получаемый урон на показатель брони
				Работа ярости: Множитель ярости влияет на скорость получение и уменьшения ярости чем больше множитель тем меньше ярость уходит а прибавляется быстрее
		
				 
			При уклонении от каких-либо атак кроме блоком повышается ярость
			При защиты блоком от ударов ты получаешь прибавку к здоровью
	
	--Создание собственного персонажа--
	--ПРИМЕЧАНИЕ-- если будет больше 8-ми персонажей то будут отображаться только первые 8
	
		--Пункт 1--
			Нарисовать анимации персонажу:
			--!!! ПРИ РИСОВАНИИ АНИМАЦИЙ У ВСЕХ КАДРОВ И У ВСЕХ АНИМАЦИЙ СДЕЛАЙТЕ ОДИНАКОВУЮ ОБЛАСТЬ РЕКОМЕНДУЕТСЯ 57 НА 61 ПИКСЕЛЬ!!!-- иначе анимация будет дёргаться
			Учтите что советуется рисовать имено столько кадров сколько написано ниже иначе вы можете сделать слишком быстрые анимации
			Если что-то не понятно можете посмотреть на файлы кадров персонажей которые уже сделаны
				стойка - не больше 13 кадров
				удар 1 - не больше 3-ех кадров
				удар 2 - не больше 3-ех кадров
				присед - не больше 2-ух кадров
				блок - не больше 2-ух кадров
				прыжок - не больше 5-ти кадров
				пробитие блока - не больше 8-ми кадров
				подножка - не более 13 кадров
			--ПРИМЕЧАНИЕ-- Советуется при создании нового персонажа скопировать существующую папку персонажа переименовать её и посмотреть структуру анимаций и поменять.
			!!!НАЗВАНИЯ КАДРОВ ИМЕНОВАТЬ НАЧИНАЯ С НУЛЯ!!!
		---Пункт 2--
			Нарисовать прочите картинки персонажей:
				иконка в меню
				надпись выигрыша
			Не стестняйтесь смотреть пример как создано у существующих персонажей
		---Пункт 3--
			Самое сложное позади
			Задача характеристик персонажа:
				1.Откройте текстовый файл heroes_data.txt в папке assets/heroes
				2.Дана структура:
				{
	    				"Blue": {
	        				"name": "Tony",
	        				"HP": 220,
	        				"DEF": 3,
	        				"DMG": 4,
	        				"RAGE": 2,
	        				"BACKGROUND_C": [0, 128, 255]
	    					}, - после нового персонажа оставьте запятую
	    				"Пример": {
	        				"name": "Напиши Имя",
	        				"HP": Напиши количество здоровья,
	        				"DEF": Напиши Множитель защиты,
	        				"DMG": Напиши Множитель урона,
	        				"RAGE": Напиши Множитель ярости,
	        				"BACKGROUND_C": [255, 51, 51] - цвет фона карточки загуглите RGB и подставьте цифры выбрав цвет
	    					}
				{
	    			Меняйте только то что вместо "Пример" - название папки с файлами персонажа и там где написано "Напиши" и цифры как в примере 255,51,51
	Всё! Персонаж готов, наслаждайтесь игрой, незабудьте сохранить текстовый документ после редактирования
	
	Если вам понравилось добавьте в избраное на гитхабе я буду рад! :)
	
