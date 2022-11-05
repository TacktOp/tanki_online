init:

    $ mods ["doroga"] = u"tanki_online"

#region image
    image image_vladM        = "mods/tanki_online/image/владпнг.png"
    image image_ii           = "mods/tanki_online/image/сявапнг.png"
    image image_ura          = "mods/tanki_online/image/Юрапнг.png"
    image image_vladP        = "mods/tanki_online/image/япнг.png"
    image image_cardoroga    = "mods/tanki_online/image/машина едем.jpg"
    image image_carVLesy2    = "mods/tanki_online/image/дорошга.jpg"
    image image_carVLesy1    = "mods/tanki_online/image/едем.jpg"
    image image_pole         = "mods/tanki_online/image/поле.jpg"
    image image_cardoroga2   = "mods/tanki_online/image/катим.jpg"
    image image_motel        = "mods/tanki_online/image/мотель.jpg"
    image image_pole2        = "mods/tanki_online/image/поле2.jpg"
    image image_pole3        = "mods/tanki_online/image/поле3.jpg"
    image image_prichep      = "mods/tanki_online/image/прицеп.jpg"
    image image_fyra         = "mods/tanki_online/image/фура.jpg"
    image image_otechMatveia = "mods/tanki_online/image/отец_матвея.png"
    image image_tachka       = "mods/tanki_online/image/1.jpg"
    image image_bereg        = "mods/tanki_online/image/2.jpg"
    image image_list1        = "mods/tanki_online/image/3.jpg"
    image image_list2        = "mods/tanki_online/image/4.jpg"
    image image_domS         = "mods/tanki_online/image/5.jpg"
    image image_gostin       = "mods/tanki_online/image/6.jpg"
    image image_ahye         = "mods/tanki_online/image/7.jpg"
    image image_cafev        = "mods/tanki_online/image/8.jpg"
    image image_ylisa        = "mods/tanki_online/image/9.jpg"
    image image_barr         = "mods/tanki_online/image/10.jpg"
    image image_loda1        = "mods/tanki_online/image/11.jpg"
    image image_pereyl       = "mods/tanki_online/image/12.jpg"
    image image_cirk         = "mods/tanki_online/image/13.jpg"
    image image_cirkv        = "mods/tanki_online/image/14.jpg"
    image image_loda2        = "mods/tanki_online/image/15.jpg"
    image image_izba1        = "mods/tanki_online/image/16.jpg"
    image image_digcaprio    = "mods/tanki_online/image/17.png"
    image image_oficnegr     = "mods/tanki_online/image/18.png"
    image image_gena         = "mods/tanki_online/image/19.png"
    image image_bomj         = "mods/tanki_online/image/20.png"
    image image_jonisini     = "mods/tanki_online/image/21.png"
    image image_izba2        = "mods/tanki_online/image/17.jpg"
    image image_sp20min      = "mods/tanki_online/image/сп20минут реальноговремент.jpg"

#endregion


#region sound
    $ sound_ptichi                   = "mods/tanki_online/sound/птици.mp3"
    $ sound_carStart                 = "mods/tanki_online/sound/car-start.mp3"
    $ sound_carEdet                  = "mods/tanki_online/sound/car-edet.mp3"
    $ sound_zvukiPrirodyKapliDozhdya = "mods/tanki_online/sound/zvuki-prirody-kapli-dozhdya.mp3"
    $ sound_zvukEzdi                 = "mods/tanki_online/sound/звук_езды.mp3"
    $ sound_sverchki                 = "mods/tanki_online/sound/звуки_сверчков.mp3"
    $ sound_skrimer                  = "mods/tanki_online/sound/skrimer.mp3"
    $ sound_rechka                   = "mods/tanki_online/sound/Sound_17860.mp3"
    $ sound_listik                   = "mods/tanki_online/sound/london-oxford-street_z1pkjle_.mp3"
    $ sound_domig                    = "mods/tanki_online/sound/f28e6f472bd6f38.mp3"
    $ sound_classikmzk               = "mods/tanki_online/sound/The Four Seasons, Op. 8.mp3"
    $ sound_obozekakoi               = "mods/tanki_online/sound/natali-o-bozhe-kakojj-muzhchina.mp3"
    $ sound_govno                    = "mods/tanki_online/sound/Султан Лагучев - Горький Вкус (megapesni.com).mp3"
    $ sound_proboi                   = "mods/tanki_online/sound/прибойПенис.mp3"
    $ sound_ytro                     = "mods/tanki_online/sound/birds-singing.mp3"
#endregion


#region name
    $ name_vladM   = Character (u'ВладМ',          color = "#60ca3f",   what_color = "#FFFFFF")
    $ name_vladP   = Character (u'ВладП',          color = "#76d4ff",   what_color = "#FFFFFF")
    $ name_ura     = Character (u'Юра',            color = "#FF8C00",   what_color = "#FFFFFF")
    $ name_ii      = Character (u'Сява',           color = "#cc5233",   what_color = "#FFFFFF")
    $ name_rem     = Character (u'Рем',            color = "#00a2ff",   what_color = "#FFFFFF")
    $ name_matvei  = Character (u'Матвей',         color = "#1e7055ff", what_color = "#FFFFFF")
    $ myzik        = Character (u'Мужик',          color = "#703c1eff", what_color = "#FFFFFF")
    $ chel         = Character (u'Чел',            color = "#050c49ff", what_color = "#FFFFFF")
    $ offnik       = Character (u'Официант негр',  color = "#000000ff", what_color = "#FFFFFF")
    $ gena         = Character (u'ШлюхаЖена',      color = "#ff00ffff", what_color = "#FFFFFF")
    $ bomg         = Character (u'Бомж',           color = "#ffffffff", what_color = "#FFFFFF")

#endregion

    transform begg:
        zoom 1.05 anchor (48, 27)
        ease 0.10 pos (0,0)
        ease 0.10 pos (25, 25)
        ease 0.10 pos (0, 0)
        ease 0.10 pos (-25, 25)
        repeat

label doroga:
    scene image_cardoroga with dissolve
    play music sound_carEdet fadein 0.5
    th "Запах старого салона в нашей Ниве очень сильно бил мне по носу, спасал только запах сырости с улицы, где на протяжении всего дня проливали дожди."
    th "Окна в машине пришлось опустить{w}, что бы не умереть от духоты."
    th "Огромных усилий стоило прокрутить эти старые ручки{w}, и теперь казалось, что опустить стекла мы уже не сможем."
    th "Мы ехали по пустой дороге{w}, из звуков был только скрежет и скрипы нашей машины{w}, ветер и звуки леса."
    th "Иногда я разбирал слова в песнях Влада{w}, которые с особой громкостью играли у него в наушниках{w}, пока сам он дремал без задних ног."
    th "Я был за рулём{w}, а Сява сидел рядом и через мой ноут, ковырял нашего бота."
    th "Юра же, читал книгу, иногда посмеиваясь."

    name_vladP "Блять, ты уже минут сорок хихикаешь, что ты читаешь там?"
    name_ura "Смари"
    th "Юра показал в зеркало заднего вида, книгу \"Феменизм наглядно 2\"."
    name_vladP "Бляяяя чувак{w}, нахуй ты взял с собой это чудовище?"
    name_ura "Всё равно в дороге делать нечего."
    name_vladP "Так всё, я заебался{w}, смените меня кто нибудь."
    name_ura "Вот пусть этот потлатый едет."
    name_ii "Не думаю что это хорошая идея{w}, не хочу откиснуть от того что сонный Влад въебёт нас в \"Камаз\"."
    name_ura "Блять, ладно{w}, сейчас из зоны лесополосы выедем и стопай."
    th "Ехали еще минут двадцать{w}, к моменту остановки, тучи разошлись.{w} Мы решили воспользоваться моментом и похавать."

    stop music fadeout 0.5
    play music sound_ptichi fadein 0.5
    scene image_pole with dissolve
    show image_ura with dissolve
    name_ura "Сява, поставь воду кипятиться."
    show image_ii at fleft with dissolve
    name_ii "Ща оформлю."
    th "Мы расстелили около подсолнухов большой плед и разложили на нем дошики и хлеб."
    name_ii "Может буданём алкаша, что бы тоже поел."
    name_ura "Да ненадо{w}, пусть спит."
    show image_vladP at right with dissolve
    name_vladP "Кста, че у тебя по практике Юра?"
    name_ura "Да эти мудаки захотели меня засунуть к старшим классам, я отказался."
    name_ii "Че так?"
    name_ura "Да они тупые как пробки, особенно девочки{w}, вроде оддинадцатый класс, а одеваются как шалавы."
    name_vladP "Хахахах{w}, ну так бомби, подцепишь какую-нибудь там."
    name_ura "Ты даун?{w} Я не настолько конченый{w}, да и в тюрьму я не хочу.{w} Да и камон{w}, это же всё ещё дети."
    name_ii "Ну поживём увидим."
    name_ura "Иди-ка нахуй."
    name_vladP "Хахахха{w}, ладно, погнали уже."
    hide image_ura
    hide image_ii
    hide image_vladP
    with dissolve
    stop music fadeout 0.5
    play sound sound_carStart fadein 0.5
    th "На ходу допив жижку от говяжего дошика, я упал на переднее сиденье, а Юра кряхтя уселся за руль."
    stop sound fadeout 0.5

    play music sound_zvukiPrirodyKapliDozhdya fadein 0.5
    scene image_carVLesy1 with dissolve
    th "Не успели мы проехать и километра{w}, как мы услышали посапывание Сявы, который наевся и спит."
    th "Вот погода опять начала хериться{w}, и палящая жара сменилась приятной свежестью."
    name_vladP "Чувак, сам проедешь?{w} А то меня в сон клонит, вздремнуть бы по хуйне."
    name_ura "Да всё оки{w}, спи."

    show blink
    th "Я заснул сразу же как закрыл глаза."
    scene image_carVLesy2
    hide blink
    show unblink
    th "Пока мы все спали, Юра двигался по узкой дороге без асфальта, которая проходила прям в чаще леса."
    th "Он взглянул на время{w}, было пол пятого."
    name_ura "Блять{w}, таблетки же нужно выпить{w}.... сука они в багажнике, это надо блять останавливаться ещё."
    name_ura "А может в пизду{w}, потом выпью{w}, хмм."
    stop music fadeout 0.5
    
    menu:
        "выпить таблетки":
            jump akt1
        "не пить таблетки":
            jump ne_vipil_tabletki


label akt1:
    scene image_cardoroga2 with dissolve
    play music sound_carEdet fadein 0.5
    th "Юра вёл тачку уже шестой час{w}, параллельно играя с нами в слова на жанры порно"
    name_ii "Мммммм{w}, ф, ф, ф{w}, наверно фистинг"
    name_vladM "Хахахах{w}, бля, что есть на Г?{w} Грязное это жанр?"
    name_ura "Не думаю{w}, называй или проебал"
    name_vladP "Блять{w}, может гейск..."
    th "Не успел Влад договорить, как нас заставил заткнуться жёсткий стук и сильный скрежет"
    name_vladP "Какого хуя?{w} Что это?"
    stop music fadeout 0.5

    play music sound_ptichi fadein 0.5
    scene image_pole2 with dissolve
    th "Юра стопнул тачку"
    show image_vladM at fleft with dissolve
    name_vladM "Пипяо{w}, только этого нам не хватало"
    th "Юра открыл капот машины, оттуда шёл дым как в гта"
    show image_vladP at left with dissolve
    name_vladP "Блять{w}, думаю всё очень хуёво{w}, че стопать будем?"
    show image_ii with dissolve
    show image_ura at cright with dissolve
    name_ii "Ну выбора у нас особого нет"
    th "Погода как будто менялась под тот пиздец который происходит, казалось, что стоит начаться ливню и с нами произойдёт какой-то кромешный пиздец"
    th "Небо полностью покрылось тучами{w}, дул уже не приятно прохладный, а весьма холодный ветер, вызывающий муражки"
    th "Влад подобно шлюхи с трассы подошел в дороге и вытянул руку"
    th "Всем было на нас настолько похуй{w}, что иногда было заметно что водители даже не смотрели в нашу сторону"
    th "Прошло минут тридцать{w}, и нам улыбнулась удача{w}, перед нами остановился грузовик"
    name_vladP "Ебать ну наконец-то"
    th "Подозрительно погода начала падлить, начинался дождь"
    show image_otechMatveia at fright with dissolve
    myzik "Ну че пацаны, встали?"
    name_ura "Есть такое"
    name_ii "Было бы классно что бы вы нас подцепили{w}, можем заплатить"
    myzik "Разберёмся{w}, трое в тачку, кто-то один ко мне пусть ныряет"
    name_vladM "Я хочу"
    th "Влад в пару мгновений запрыгнул на пассажирское сиденье огромной фуры{w}, а мы с кентами залетели в тачку"
    stop music fadeout 0.5

    play music sound_zvukEzdi fadein 0.5
    scene image_fyra with dissolve
    show image_vladM at fleft
    show image_otechMatveia at fright 
    with dissolve
    myzik "Вас до куда?"
    name_vladM "Тут где-нибудь есть мотель и сто?"
    myzik "Да в паре часов езды есть комплекс мотелей, там же и сто"
    name_vladM "Вот туда нам надо"
    myzik "Лады"
    th "Погода была омерзительней некуда{w}, дождь лил как из ведра"
    th "Влад задремал{w}, и не прошло для него как будто бы и пары минут, как он ощутил похлопывание по плечу"
    stop music fadeout 0.5
    myzik "Малой вставай{w}, приехали"
    th "Влад моментально очнулся"
    name_vladM "Да{w}, спасибо{w}, ща гляну по деньгам"
    th "Влад достал кошель и начал перебирать наличку, что бы отблагодарить нашего спасителя"
    myzik "Знаешь....{w}, я бы не сказал что мне нужны деньги"
    name_vladM "ээ{w}, ну может вас угостить чем-то?"
    myzik "Ну{w}, угостить ты меня можешь"
    play music music_list['doomed_to_be_defeated'] fadein 0.5
    show image_otechMatveia at left with dspr
    th "И произошло то, чего ожидать Влад не мог никак{w}, мужик начал поглаживать его по коленке и вести руку к письке"
    name_vladM "ЭЭЭЭ{w}, ТЫ ЧЕГО ТВОРИШЬ?{w} ИДИ НАХУЙ МУДАК ЁБАНЫЙ"
    th "Влад попытался выйти из машины{w}, но двери оказались закрыты"
    myzik "ТЫ НЕ КУДА НЕ ПОЙДЁШЬ"
    th "Мужик схватил его руку{w}, а второй взял за горло"
    name_vladM "*задыхаясь* ссука{w}, ты что творишь..."
    myzik "Беру расплату за поездку"
    th "Он принялся расстёгивать ему ширинку"
    stop music fadeout 0.5
    
    play music sound_sverchki fadein 0.5
    scene image_motel with dissolve
    show image_ii
    show image_ura at right
    show image_vladP at left
    with dissolve
    name_vladP "Так{w}, тачка вроде всё{w}, я в ахуе что там была такая мелочь"
    name_ura "Да не говори{w}, кста, а Влад где?"
    name_ii "Вроде бы он расплачивается с водилой{w}, но чёт долго"
    name_ura "Надо глянуть, вдруг случилось что то"
    th "Они начали подходить к машине и приближаясь{w}, всё чётче слышали истошные попытки вздохнуть и какую-то возню"
    name_ii "Чё за херня?"
    name_vladP "А там не Влада пиздят?"
    name_ii "ПОГНАЛИ"
    stop music fadeout 0.5
    play music music_list['doomed_to_be_defeated'] fadein 0.5

    scene image_fyra
    show image_vladM at fleft
    show image_otechMatveia at left 
    with dissolve
    th "Открыв дверь мы увидели то{w}, как мужик судорожно держа Влада за горло пытался изнасиловать его{w}, но Юра выкинул мужика из машины"

    scene image_motel with dissolve
    show image_ura 
    show image_otechMatveia at left
    with dissolve
    name_ura "Ты чё мудила, ахуел?"
    th "Не прошло и секунды как Юра со всей силы дал лежащему на земле мужику под дых" with hpunch
    hide image_otechMatveia with dspr
    show image_vladP at left
    show image_ii at fleft 
    with dissolve
    name_vladP "Всё норм чувак?"
    show image_vladM at fright with dissolve
    name_vladM "*тяжело дыша* да{w}, пидор ёбаный"
    th "Мужик попытался что-то сказать{w}, но Сява предотвратил это, пнув его по голове и вырубив его нахер"
    stop music fadeout 0.5
    play music sound_sverchki fadein 0.5
    name_ii "Уёбище тупорылое{w}, погнали чекнем что у него в контейнере{w}, может за моральную компенсацию прихватим чё нить"
    name_ura "Го"
    stop music fadeout 0.5
    play music sound_sverchki fadein 0.5
    scene image_prichep with dissolve
    show image_ii at right 
    show image_ura 
    show image_vladM at left
    show image_vladP at fright
    with dissolve
    th "Мы обошли машину и открыли двери огромного, длинного прицепа"
    th "Перед нами появилась картина{w}, около двухста ноутбуков, коробки с которыми, лежали ровно друг на друге в несколько рядов"
    name_vladP "Думаю{w}, за ту хуйню которую он сделал, мы имеем права позаимствовать три ноута"
    name_vladM "Не,{w} ну а чё?"
    th "В эту же секунду Сява подал Юре стопку из трёх ноутбуков"
    name_ura "Балдёж{w}, ебать они кста тяжёленькие"
    name_ii "Да{w}, марка наверно такая"
    name_vladM "Так{w}, думаю пока он не очнулся, было бы неплохой идеей свалить прямо сейчас{w}, тем более тачка готова{w}, поведу - я{w}, мне сейчас уж точно не до сна"
    name_ura "Ну поехали"
    th "Мы сели в тачку{w}, и погнали прочь от этого мотеля"
    
    play music sound_carEdet fadein 0.5
    scene image_pole3 with dissolve
    th "Мы ехали уже несколько часов{w}, Влад всё также вёл машину, я проснувшись ещё час назад, болтал с ним{w}, а Юра с Сявой дрыхнули, юзая как подушку дакимакуру Влада"
    name_vladM "Бля{w}, жду не дождусь приезда туда{w}, хочу пьяный купаться в Байкале"
    name_vladP "Там такая холодрыга{w}, все яйца себе отморозишь"
    name_vladM "Да я ж пьяный буду{w}, мне жарко будет"
    name_vladP "Хахахах"
    name_ii "*зевая* ооой бля{w}, как же ахуенно"
    name_vladP "С добрым брат"
    name_ii "Ага{w}, о чём тут базарите?"
    name_vladP "Влад хочет пьяный в Байкале искупаться"
    name_ii "Я почему-то не удивлён"
    name_ura "Бля{w}, давайте когда приедем, сразу купаться пойдём"
    name_vladP "Хахахах{w}, ты погоду видел?{w} В первые дня два нашего приезда, погода будет просто пиздец"
    name_ii "Не, если ты хочешь искупаться и так в ледяном байкале да ещё и в плюс тринадцать{w}, пожалуйста"
    name_vladP "Только потом опять будешь свой Терафлю искать и хлестать"
    th "Так мы общались ещё часами, но в какой-то момент мы заметили остановку"
    name_vladM "Чуваки{w}, там какая-то остановка"
    name_vladP "Что-то я не помню{w}, что бы по пути у нас была деревня или село"
    name_ii "Гляньте по навигатору"
    name_vladM "Ой...."
    th "Через этот ой я сразу понял что произошла какая-то хуйня"
    name_vladM "Ну{w}, мы кажись навигатор оставили в мотеле на зарядке"
    name_vladP "Пиздец{w}, балдёж"
    name_ura "Как варик остановиться здесь и поискать людей{w}, может у них есть навик, ну на крайняк карта"
    name_vladM "Оки{w}, стопаю"
    stop music fadeout 0.5
    
    play ambience ambience_camp_center_day fadein 0.5
    scene bg ext_camp_entrance_day with dissolve
    th "Мы остановились у остановки и перед нами развернулись большие ворота ведущие на какую-то территорию"
    name_vladP "Хм{w}, выглядит как....{w} летний лагерь"
    name_ii "Больше на пионерский похож"
    th "Мы с Сявой и Юрой рассуждали и предпологали что может там скрываться и один Влад задумчиво глядел на чуть ржавые ворота"
    name_vladM "У меня какое-то очень странное ощущение{w}, как будто что-то мне это напоминает"
    name_vladP "Что именно?"
    name_vladM "Не могу объяснить{w}, ощущение будто был здесь{w}, но точно не был"
    name_ii "Дежавю{w}, А МОЙ ПЛЕЙС БЕФОРЕС АЙЯАЯАЯАЯ ЭЧТИ СИ"
    name_vladP "Дуракич"
    name_ura "Ну что{w}, погнали?"
    th "И только мы подошли к воротам{w}, к нам вышла девочка"
    show sl normal pioneer with dissolve
    sl "Привет, вы, наверное, только что приехали?"
    name_ura "Да, привет{w}, у нас проблема с маршрутом, мы проебали навик{w}, у вас не найдётся чего нибудь подобного{w}, может карта?"
    sl "Дай подумать{w}, карта есть{w}, но она у Ольги Дмитриевны, а она сейчас занята"
    name_vladP "Блять"
    show sl tender pioneer with dspr
    sl "Пойдём со мной{w}, покажу вам лагерь, пока Ольга Дмитриевна занята"
    name_ii "Ну пошли{w}, хули делать"
    th "Мы вошли во внутрь"

    scene bg ext_clubs_day with dissolve
    th "Буквально через пятьдесят метров слева словно из-под зесли выросло небольшое одноэтажное здание"
    show cg d1_grasshopper with dissolve
    play music music_list['i_want_to_play'] fadein 0.5
    th "Перед нами открылась картина{w}, малолетняя пиздючка пугала фиолетововолосую девочку кузнечиком"
    un "Ииии-иииии-иии"
    hide cg d1_grasshopper with dissolve
    show un scared pioneer at left 
    show us laugh pioneer at right
    with dissolve
    name_ii "ЭЭЭ{w}, АЛО{w}, ЗАЛУПА МЕЛКАЯ"
    show us fear pioneer at right with dspr 
    th "Малявка резко остановилась"
    name_ii "Убери от неё это чудовище ебаное"
    show us angry pioneer at right with dspr 
    us "А ты вообще кто?"
    name_vladP "Насиловать будем"
    show us fear pioneer at right with dspr 
    th "Она испугалась и убежала, сверкая пятками"
    hide us fear pioneer with dspr
    show un shy pioneer at left with dspr
    un "Сс..с{w}..спасибо"
    name_ii "Блять да что за дети пошли{w}, ведут себя как черти, если ещё доебётся обращайся"
    show un smile pioneer at left with dspr
    th "Её глаза засверкали"
    un "Хорошо{w}, ещё раз спасибо"
    th "И она убежала в ту же сторону что и эта пиздень"
    hide un smile pioneer with dissolve
    stop music fadeout 0.5

    scene bg ext_houses_day with dissolve
    th "Мы прошли дальше и оказались среди домиков"
    th "Молча разглядывая лес{w}, я был обескуражен этим спокойствием и тишиной этого места{w}, но вдруг"
    play sound sfx_body_bump
    th "Край моего глаза увидел как нечто ударило Влада по спине и он упал на асфальт" with vpunch
    name_ii "Ээээ{w}, какого хуя?"
    show dv rage pioneer with dissolve
    th "Но перед нами только стояла рыжеволосая девочка"
    dv "Челюсти с пола поднимите"
    show dv grin pioneer with dspr
    name_vladP "Ебало сузь"
    dv "Вы новенькие значит?"
    name_ii "Нет{w}, у нас с маршрутом беда"
    dv "Ясно{w}, а кто вас сопровождает?"
    th "И действительно{w}, та девочка у ворот просто исчезла{w}, мы гуляли сами по себе"
    name_ura "Сами себя сопровождаем"
    dv "Ладно{w}, увидимся"
    hide dv grin pioneer with dspr
    th "И она убежала"
    name_vladP "Блять{w}, хули все нас так шугаются{w}, не уж то мы настолько уроды?"
    th "Пацаны лишь пожали плечами"
    th "Мы решили пойти дальше"
    name_vladP "ОООООО{w}, ТАМ ОЗЕРО!"
    name_ura "Ебааааать"
    stop ambience fadeout 0.5
    
    play ambience ambience_boat_station_day fadein 0.5 
    scene bg ext_boathouse_day with dissolve
    th "Мы прибежали к пристани{w}, шум ветра и воды делал это место практически райским"
    show sl normal swim with dissolve
    sl "Ой{w}, так вам не сюда!"
    th "Перед нами оказалась та самая девочка, которая встретила нас у ворот{w}, но в этот раз на ней кроме купальника ничего не было"
    name_vladP "Уфффф{w}, ебать"
    show sl smile swim with dspr
    sl "Кстати{w}, а как вас зовут?"
    name_vladP "Я Влад"
    name_ura "Юра"
    name_ii "Слав.."
    name_vladP "Сява{w}, его зовут Сява"
    sl "А тебя?"
    th "Но Влад молчал{w}, по нему было видно что его что-то тревожит, всё это место не давало ему покоя"
    name_ura "Это Влад"
    sl "Ого{w}, вас двое"
    name_vladP "А тебя как?"
    sl "Вообще{w}, полное имя Славяна, но все меня Славей зовут"
    name_vladP "Ебать прикол{w}, у нас тоже свой Славя есть{w}, только с хуем"
    show sl smile2 swim with dspr
    th "Она смущённо усмехнулась"
    sl "Так{w}, идите на площадь{w}, я преоденусь и встречу вас там"
    name_vladP "Можешь пойти так"
    show sl shy swim with dspr
    th "Они покраснела{w}, а я понял что кажется я - даун"
    stop ambience fadeout 0.5
    
    play ambience ambience_camp_center_day fadein 0.5
    scene bg ext_square_day 
    show dv normal pioneer at left
    show us normal pioneer at right
    with dissolve
    th "Мы вышли на площадь{w}, по середине которой стояла статуя пионера"
    th "Там мы обнаружили две ахуевшие дуры{w}, с которыми нам уже посчастливилось стретиться"
    dv "О{w}, это же вы"
    show us fear pioneer at right with dspr
    us "Это эти насильники!"
    dv "Чего???"
    name_ura "Нам надо было как то прогнать эту падаль{w}, вот и сказали что ща на четверых растянем"
    show dv angry pioneer at left with dspr
    dv "Вы блять больные!"
    name_vladP "ахах..хахахаха...{w}ХАХАХАХХАХАХ"
    th "Для зловещности{w}, я засмеялся как психопат"
    name_ii "Хахах{w}, прекращай{w}, а то никакой карты мы не получим"
    show sl normal pioneer close with dissolve
    sl "О{w}, вы уже здесь"
    sl "Ольга Дмитриевна свободна{w}, пойдём до её домика"

    scene bg ext_house_of_mt_day with dissolve
    th "Через пару минут мы оказались у треугольного домика, вокруг которого росла черёмуха"
    
    stop ambience fadeout 0.5
    play music music_list['so_good_to_be_careless'] fadein 0.5
    scene bg int_house_of_mt_day
    show mt normal pioneer 
    with dissolve
    play sound sfx_open_dooor_campus_1 
    th "Мы вошли{w}, перед нами стояла девушка лет двадцати пяти{w}, Юра заприметил на полу мусорное ведро, а рядом с ним лежала упаковка из под шоколадки{w}, нахой он это сделал незнаю{w}, но он поднял бумажку, смял её и выбросил в мусорку"
    mt "Привет{w}, вы новенькие?"
    name_vladP "ДА БЛЯТЬ НЕТ{w}, у нас навигатор...сломался{w}, нам нужна карта"
    mt "ааа{w}, хорошо, у меня есть как раз{w}, держите"
    name_ii "Ого{w}, вот так просто"
    show mt smile pioneer with dspr
    mt "А вы торопитесь?"
    name_ii "Ну..{w} да нет"
    mt "Ну так может останетесь на ночь у нас{w}, а то уставшие, а завтра полные сил поедите"
    stop music fadeout 0.5
    name_vladP "Хм{w}, а знаете, было бы неплохо"
    th "Лицо Влада резко побелело"
    play sound sound_skrimer
    show cg epilogue_mi_2
    $ renpy.pause(0.4)
    hide cg epilogue_mi_2
    name_vladM "Пацаны{w}, выйдем"
    play sound sfx_open_dooor_campus_2

    play ambience ambience_camp_center_day fadein 0.5
    scene bg ext_house_of_mt_day with dissolve
    th "Мы вышли на улицу"
    name_ura "Что такое чувак?"
    th "Влад был весь бледный, но при этом мокрый"
    name_vladM "Мы не можем здесь остаться"
    name_vladP "Почему?"
    name_vladM "Это чувство не покидает меня{w}, будто я здесь провёл не один час{w}, ни два{w}, ни сто{w}, больше!"
    name_ii "Блять{w}, может тебе сон приснился или просто крыша едет{w}, ты здесь не был никогда"
    name_vladP "Кароче, остаёмся"
    name_vladM "сука{w}, пойду прогуляюсь"
    name_vladP "Давай{w}, я наврено по лесу пройдусь, всегда хотел в сумерках погулять по лесу"
    th "А ведь правда{w}, мы потратили довльно много времени здесь, что уже начало смеркаться"
    name_ii "А я хочу пойти поискать ту девочку с фиолетовыми волосами"
    name_ura "Блять, да вы сговорились{w}, а мне что делать?"
    name_ii "Иди спать, твоя очередь завтра тачку вести"
    name_ura "ДА СУКА!{w} СУКА{w} СУКА"
    th "Юра понимал что выбора у него другого нет и ему реально пришлось идти спать"

    scene bg ext_square_night with dissolve
    th "Тем временем у Сявы"
    stop ambience fadeout 0.5
    
    play ambience ambience_camp_center_night fadein 0.5
    play music music_list['lets_be_friends'] fadein 0.5
    show cg d6_un_evening_2 with dissolve
    th "Лена сидела на скамейке и читала книгу"
    name_ii "ээ{w}, привет"
    un "привет"
    name_ii "Ты почему тут сидишь одна{w}, что читаешь?"
    un "Люблю вечерами почитать{w}, это Джек Лондон{w}, а ты что нибудь читаешь?"

    show cg d6_un_evening_1 with dissolve
    th "Сяве было стыдно признать тот факт что он книгу последний раз держал в садике{w}, но выпалил.."
    name_ii "Маяковского люблю"
    un "Здорово{w}, я тоже, какое твоё любимое произведение?"
    th "Сява понимал что единственное произведение Маяковского он знал, это \"Вы любите розы?\""
    name_ii "Ну{w}, мне наверно все нравятся"
    th "В ответ Лена лишь посмеялась"
    th "Сява думал лишь о том, что он никогда в жизни не видел настолько скромной девочки{w}, она была будто из книги"

    show cg d6_un_evening_2 with dissolve
    un "Слава"
    un "Можешь трахнуть меня?"
    th "У Сявы зазвенело в ушах и ноги стали ватными"
    name_ii "Чего?"
    un "Ну мы пойдём ко мне в домик и потрахаемся"
    name_ii "Аааа{w}, мы же с тобой только познакомились"
    un "Ну смотри, ты мне понравился и я тебе{w}, завтра ты уедешь{w}, так может оторвёмся?"
    th "С Сявой говорил как будто другой человек{w}, та девочка с которой Сява говорил минуту назад просто испарилась"
    name_ii "Ну пошли:)"
    
    show cg d7_un_hentai with dissolve
    show cg d7_un_hentai_3 with dissolve
    th "Следующую ночь Сява провёл с девушкой, которую он знал всего лишь один день{w}, но этот секс Сява запонил точно на всю жизнь"
    stop music fadeout 0.5
    stop ambience fadeout 0.5

    play ambience ambience_forest_night fadein 0.5
    scene bg ext_path_night with dissolve
    th "Я шёл по лесу{w}, птицы уже не пели{w}, слышно было только сверчков и шум листьев"
    th "По увеличению количества мошки, я понимал что приближаюсь к какому-то водоёму"
    th "Тут я услышал шорохи{w}, спрячась за кустом, я смотрел в сторону пруда"

    show cg d2_slavya_forest with dissolve
    th "Это была Славя{w}, она шла около пруда и постепенно снимала с себя одежду"

    show cg d2_sl_swim with dissolve
    th "И вот уже полностью голая Славя заходила в пруд"

    show cg d6_sl_swim with dissolve
    th "Окликнуть её было бы странным мувом{w}, но и уходить как-то не хотелось"
    th "Я просидел так ещё минут двадцать, и дождался момента, когда она вышла из воды"
    th "Она оделась, а я постепенно начал уходить"
    th "Я гуськом добрался до другого дерева и уже собирался бежать как вдруг"
    play music music_list['i_dont_blame_you'] fadein 0.5 

    show cg d6_sl_forest with dissolve
    sl "Эй{w}, привет!"
    th "Блять!{w} БЛЯТЬ!"
    name_vladP "Ээаэаэ{w}, привет"
    th "Она подошла и села рядом"
    sl "Ты всё видел?"
    name_vladP "аа{w}, что видел?"
    sl "Меня без одежды"
    name_vladP "Нее{w}, я только пришёл"
    sl "Я заметила тебя ещё когда заходила в воду"
    name_vladP "ЧЕГО?{w} И почему ничего не сказала?"
    sl "Нуу{w}, за мной ещё не подглядывали мальчики"
    name_vladP "Ну значит я перв.."
    th "И вот я не договорил и почувствовал странное чувство{w}, он поцеловала меня"
    sl "Понравилось?"
    th "Мой внутренний девственник чувствовал{w}, что нужно продолжения, но что делать я не знал"

    show cg d6_sl_hentai_2 with dissolve
    th "Я положил ей руку грудь"
    th "Она смущённо опять поцеловала меня"

    show cg d6_sl_hentai_1 with dissolve
    th "Дальше всё пошло само по себе{w}, мы трахались пол ночи"

    show cg d7_sl_morning with dissolve
    th "Закончив, мы легли спать в спальный мешок"
    stop ambience fadeout 0.5
    stop music fadeout 0.5

    play ambience ambience_camp_center_night fadein 0.5
    scene bg ext_houses_sunset with dissolve
    th "Влад шёл по лагерю сам не свой{w}, эта тревога не покидала его"
    play sound sfx_body_bump
    th "Тут он почувствовал сильный толчок в спину и упал на траву" with vpunch
    show dv angry pioneer with dissolve
    dv "Опять ты!"
    name_vladM "Сука!{w} Куда ты вечно торопишься?{w} Почему за этот день ты уже второй раз сшибаешь меня с ног?"
    show dv normal pioneer with dspr
    dv "Я убегаю"
    name_vladM "Блять{w}, от кого?"
    dv "Я кое-что спёрла из столовой"
    name_vladM "По тебе и не скажешь, что ты любишь поесть на ночь"
    show dv laugh pioneer with dspr
    dv "Я спёрла это"
    th "Алиса достала бутылку на которой было написано \"Водка Столичная\""
    name_vladM "Ого"
    dv "Так и быть{w}, за твоё молчание предлагаю выпить вместе"
    name_vladM "Балдёж{w}, пойдём"
    stop ambience fadeout 0.5

    scene bg int_house_of_dv_night 
    show dv normal pioneer
    with dissolve
    play music music_list['she_is_kind'] fadein 0.5
    play sound sfx_open_dooor_campus_1 
    th "Они зашли в домик, в котором никого не было"
    th "Усевшись за стол они начала глушить водку{w}, стопку за стопкой"
    show dv grin pioneer2 with dspr
    dv "*икая* А хороший ты парень Влад"
    name_vladM "Ты тоже нич *ик* ё, такая"
    dv "А ты девственник?"
    name_vladM "Я?{w} Да я ебался больше чем ты живёшь"
    dv "Вау{w}, значит покажешь мне как это?"
    show dv shy body with dspr
    th "Влад и не заметил того как Алиса полностью разделась"
    dv "Ну что, давай"
    th "Естственно Влад был самым девственным девственником в истории{w}, поэтому пришлось импровизировать"
    th "Одной рукой он начал мацать сиськи, а второй полез в пизду"
    show dv surprise body with dspr
    dv "Аххх"

    show cg d6_dv_hentai with dissolve
    th "Я как рассказчик хуй знает какого лешего в этом парте так много секса, ну раз подвернулся случай, почему бы и нет"

    show cg d6_dv_hentai_2 with dissolve
    th "На протяжении ночи Влад трахал Алису{w}, пока они не уснули вместе"
    stop music fadeout 0.5

    play ambience ambience_forest_day fadein 0.5
    scene bg ext_path_day with dissolve
    th "Утром солнце светило особенно ярко{w}, я хотел приобнять Славю, но со мной в мешке её не оказалось"
    th "Странно{w}, наверно уже ушла в лагерь"
    stop ambience fadeout 0.5

    play ambience ambience_camp_center_day fadein 0.5
    scene bg ext_house_of_sl_day with dissolve
    th "Я пришёл к нашему домику, на улице стояли Юра и Влад"
    name_ura "О, ты в лесу что ли ночевал?"
    name_vladP "Пацаны{w}, ща ахуеете{w}, угадайте кто вчера натянул Славю"
    name_ura "ДА ВЫ АХУЕЛИ!{w} Влад тоже вчера с Алисой развлекался"
    name_vladP "Ооооо{w}, легенда чел"
    th "Я дал Владу краба"
    name_ura "Блять{w}, где Сява?{w} Если он сейчас придёт и окажется что он тоже кого то трахал вчера, то я ливаю хз как это контрить бб не будет"
    name_ii "Всем привет"
    name_ura "Ты трахался вчера?"
    name_ii "Откуда ты узнал?"
    th "Лицо Юры было похоже на лицо человека, который пропустил какой-то трушный тусич"
    name_ii "Только она утром ушла куда-то, я её даже не видел"
    name_vladP "Моя кстати тоже"
    name_vladM "Алиса тоже ушла куда-то"
    name_ura "Ну они то в лагере{w}, так что не удивительно"
    name_vladP "Ладно{w}, бери карту Юра и поехали"

    scene bg ext_square_day with dissolve
    th "Мы вышли на площадь и к нам подошла Славя"
    show sl normal pioneer with dissolve
    sl "Привет, вы, наверное, только что приехали?"
    play sound sound_skrimer
    show cg epilogue_mi_7
    $ renpy.pause(0.4)
    hide cg epilogue_mi_7
    name_vladP "Смешно красавица{w}, ну ладно мы покатили"
    play sound sound_skrimer
    show cg d7_un_suicide
    $ renpy.pause(0.4)
    hide cg d7_un_suicide
    th "Я поцеловал её"
    show sl scared pioneer with dspr
    sl "Что ты делаешь дурак!"
    hide sl scared pioneer with dspr
    th "Она покрасневшая убежала"
    th "Я повернул голову в тот момент когда пацаны уже пытались привести Влада, лежащего на земле, в чувства"
    name_vladP "Что случилось?"
    name_ii "Обморок"
    name_vladM "Пацаны{w}, она не шутила{w}, происходит то о чём я и думал{w}, это не у меня крыша едет"
    name_ura "О чём ты?"
    name_vladM "Я не понимаю от куда я это знаю{w}, но мы кажется попали в день сурка"
    name_ii "Не{w}, крыша всё таки поехала"

    scene bg ext_no_bus with dissolve
    th "Сява закинул Влада на плечо и кинул на заднее сиденье"
    name_vladP "Трогай Юржи"
    th "Юра завёл машину и мы поехали"
    
    scene bg ext_road_day with dissolve
    name_vladM "Пацаны поверьте{w}, нам не стоит вот так просто уезжать"
    th "Мы ехали уже минут двадцать{w}, я будучи выспашимся, почему-то зевал, а Сява с Владом и вовсе давали храпака"
    name_vladP "Чувак{w}, я чуть вздремну{w}, смотри не усни"
    th "Меня вырубило сразу{w}, но я даже не подозревал, что Юра прям за рулём, уснёт спустя буквально пару минут"
    show blink
    th "Его глаза медленно закрывались, и тут..."
    stop ambience fadeout 0.5

    scene bg int_house_of_sl_day
    hide blink
    show unblink
    name_ura "АААААААААААА"
    name_vladP "*зевая* ааа{w}, что такое?"
    name_ura "МЫ ЕХАЛИ В МАШИНЕ"
    name_vladP "А что та...."
    th "Я протёр глаза и увидел{w}, мы в том домике, в котором ночевали, в том самом лагере"
    th "Если Сява просто молча ахуевал от происходящего, то Влад..."
    name_vladM "СУКА Я ГОВОРИЛ! Я ГОВОРИЛ БЛЯТЬ!{w} ЭТО ЕБУЧИЙ ЦИКЛ"
    name_ii "Я думаю всему этому должно быть разумное объяснение{w}, давайте сходим к домику Ольги"

    scene bg ext_house_of_mt_day with dissolve
    th "По пути мы на удивление никого не встретили{w}, а вскоре оказались у её домика"
    
    scene bg int_house_of_mt_day
    show mt normal pioneer
    with dissolve 
    play sound sfx_open_dooor_campus_1
    play music music_list['so_good_to_be_careless'] fadein 0.5
    mt "Привет ребята, вы новенькие?"
    name_ii "Нет{w}, какого лешего?"
    show mt shocked pioneer with dspr
    mt "Что?"
    th "Пока Сява пытался донести что-то до Ольги, я взгялнул на Юру"
    th "Его лицо было бледное как пепел"
    name_vladP "Что такое чувак?"
    name_ura "*шёпотом* чувак....."
    stop music fadeout 0.5
    th "Он указал пальцем на мусорное ведро, около него лежала та самая упаковка из под шоколадки, не смятая и ВОЗЛЕ ВЕДРА БЛЯТЬ, А НЕ В НЁМ"
    name_vladP "Твою мать..."
    play music music_list['doomed_to_be_defeated'] fadein 0.5
    name_vladP "ОЛЬГА МАТЬ ВАШУ КАКОГО ХУЯ?"
    show mt rage pioneer with dspr
    mt "Прекратите кричать"
    name_ii "Так{w}, иди нахуй"

    scene bg ext_house_of_mt_day with dissolve
    play sound sfx_open_dooor_campus_2
    th "Мы вылетели из её домика"
    name_vladM "Я говорил{w}, Я ГОВОРИЛ БЛЯТЬ"
    name_vladP "И ЧТО НАМ ДЕЛАТЬ БЛЯТЬ?"
    stop music fadeout 0.5
    play ambience ambience_camp_center_day fadein 0.5
    name_ura "Так{w}, спокойствие{w}, может это всё ещё пранк"
    th "По голосу Юры было слышно, что он уже сам не верит в то что говорит"
    show dv normal pioneer with dissolve
    dv "О{w}, привет парни{w}, новенькие?"
    name_ura "Будь так добра{w}, иди уебись об дерево"
    show dv angry pioneer with dspr
    dv "Ты чё ахуел?"
    name_vladP "Метнулась от сюда падаль"
    hide dv angry pioneer with dspr
    name_ii "Так, ну спать я не хочу, могу повести машину"
    name_vladM "Сомневаюсь что это поможет"
    name_ura "У тебя есть ещё варианты?"

    scene bg ext_road_day with dissolve
    th "Не прошло уже и десяти минут как мы ехали в километре от лагеря"
    name_vladP "Так Сява{w}, всё норм?"
    name_ii "Всё ок, спать не хочется вооб..."
    show blink
    th "Резко всё потухло"
    scene bg int_house_of_sl_day
    hide blink
    show unblink
    stop ambience fadeout 0.5
    name_ura "АААААААААА"
    name_vladP "Мать вашу"
    name_vladM "Сука{w}, мы теперь навсегда здесь?"
    name_vladP "Без паники{w}, мы здесь точно не останемся, что нибудь придумаем"
    name_ura "Итак{w}, какие варианты?{w} Попробуем все"
    name_ii "Может нам нужно
    прожить день по их правилам?{w} Стать пионерами"
    name_ura "Как вариант{w}, ещё идеи"
    name_vladP "У меня есть варик, но безопасный ли он{w}, я хуй знает"
    name_ura "Какой?"
    name_vladP "Кто-то один останется здесь, а остальные попробуют уехать, может эта система сломается"
    name_vladM "Звучит как то, что может сработать"
    name_vladM "У меня не особо есть варианты"
    name_ura "Так{w}, тогда с начала действуем по плану Сявы{w}, живём день так, как хотят они"
   
    scene bg ext_house_of_sl_day with dissolve
    play sound sfx_open_dooor_campus_2
    play ambience ambience_camp_center_day fadein 0.5
    th "Мы оделись и вышли на улицу"
    show sl normal pioneer with dissolve
    sl "Привет, вы, наверное, только что приехали?"
    name_vladP "Да{w}, мы новенькие"
    sl "Это прекрасно{w}, тогда пройдём со мной к Ольге Дмитриевне{w}, она ознакомит вас со всем"
    th "Мы сами не верили в то что делаем, но выбора у нас особо не было"

    scene bg ext_house_of_mt_day
    show mt normal pioner 
    with dissolve
    mt "Здравствуйте ребята{w}, теперь вы пионеры, прошу ознакомиться с правилами и расписанием"
    th "Расписание было типичное, зарядка, обеды, ужины, общественно-полезные работы и тому подобное"

    scene bg ext_boathouse_day with dissolve
    stop ambience fadeout 0.5
    play ambience ambience_boat_station_day fadein 0.5
    th "Мы пошли к пристани"
    name_ii "Не мужики{w}, идея липа{w}, я хуйню придумал, я жалею что предложил"
    name_ura "Хахахах{w}, тебя условие подъёма в семь не устроило?"
    name_ii "И оно тоже{w}, да и логики в этом нет{w}, надо тестить план Влада"
    name_vladM "Я останусь{w}, а вы едьте"
    name_ura "Ты уверен?"
    name_vladM "Да какая разница, если не получится то все рестартнемся"
    name_vladP "А если получится, как мы тебя заберём?"
    name_vladM "Разберёмся, езжайте"
    th "Тянуть резину мы не стали{w}, прыгнули в машину и поехали"
    stop ambience fadeout 0.5

    play ambience ambience_camp_center_day fadein 0.5
    scene bg ext_road_day with dissolve 
    th "Я был за рулём{w}, ноги еле нажимали на педали{w}, они подкашивались так, как будто я стою на краю пропасти"
    name_ura "Чувак, всё норм?"
    name_vladP "Да вроде бы"
    show blink
    name_ii "Главное не засн..."
    stop ambience fadeout 0.5
    scene bg int_house_of_sl_day
    hide blink
    show unblink
    th "Стоило мне моргнуть{w}, и я открыл глаза в домике"
    name_vladP "Блять{w}, не сработало"
    name_ii "Влад{w}, нихуя не получилось"
    th "Но произошло странное{w}, Влад стоял перед нами, ноги подкашивались, а в глазах сверкали наварачивающиеся слёзы"
    name_vladP "Чувак, не бойся{w}, придумаем что нибудь"
    name_vladM "Где....{w} где вы{w}...где вы были?"
    th "Его голос дрожал"
    name_ura "Всмысле?{w} мы попыталсиь уехать, но опять проснулись здесь"
    name_vladM "Для вас прошло несколько минут?"
    name_ii "К чему ты это?"
    th "Влад завернул рукав своей толстовки"
    play music music_list['drown'] fadein 0.5
    name_ura "Мать твою"
    th "На его руке были выцарапаны полосы"
    name_vladP "Чувак{w}, сколько дней ты уже здесь?"
    name_vladM "Я проживаю этот день уже пятьдесят четвёртый раз"
    name_vladP "ЧЕГО БЛЯТЬ?"
    name_ura "Это ебучее место ломает все законы времени, пространства и логики"
    name_ii "И что ты делал эти пятдесят четыре дня"
    name_vladM "Я пробовал всё{w}, я трахал каждую в этом лагере включая Ольгу и Ульяну"
    name_vladM "В один из дней я перерезал весь лагерь, но мне всё равно пришлось доживать этот день в лужах крови, что бы опять проснуться тут"
    name_vladM "А в один из дней повесился{w}, и знаете что?{w} НИЧЕГО"
    name_vladM "Я вскрывал вены в ванне{w}, и опять по новой"
    name_vladP "Мужик, блять господи, это же пиздец"
    name_vladM "Я думал что у вас получилось и вы просто уехали"
    name_ii "Не неси хуйни{w}, мы бы лучше сдохли чем так поступили"
    name_ura "Но для нас реально прошло двадцать минут"
    name_vladM "Что бы не происходило в этом лагере{w}, потом всё возварщается обратно{w}, к самому началу"
    name_vladM "В один из дней{w}, я взорвал котёл в столовой и лагерь практически сгорел до тла{w}, стоило мне лечь спать, я просыпался в домике как ни в чём не бывало"
    name_ii "А ты пробовал не ложится спать?"
    name_vladM "Да{w}, но рано или поздно ты всё равно засыпаешь..."
    stop ambience fadeout 0.5
    th "Каждую новую идею по тому как выбраться от сюда рушил Влад{w}, он перепробовал все варианты"
    name_ii "Пойдем к Ольге, пока её нет, пороемся в её вещах, вдруг алкашку найдём"

    scene bg int_house_of_mt_day with dissolve
    play music music_list['so_good_to_be_careless'] fadein 0.5
    th "Так мы и поступили, уже через минуту мы искали всякое в домике Ольги"
    name_ii "О{w}, её трусики"
    name_vladP "Хахаха{w}, балдёж"
    name_ura "Пиздец вы кончено"
    name_ura "О{w}, отсюда она карту нам доставала"
    th "Сказал Юра, открыв ящик встроенный в стол"
    name_ii "А сама карта где?"
    name_vladM "Ну мы же её в наш ящик положили"
    th "И тут время остановились, мы с парнями
    переглянулись в надежде понять что все подумали об одном и том же"
    name_ii "А разве..."
    name_vladP "Ведь в начале карта у неё"
    name_ura "Так{w}, кажется что то нащупали{w}, бежим"
    stop music fadeout 0.5

    scene bg int_house_of_sl_day with dissolve
    play sound sfx_open_dooor_campus_2
    th "Юра первым забежал в наш домик и начал судорожно рыскать в шкафчиках{w}, и нашёл"
    name_ura "Пацаны{w}, вот она"
    name_vladM "Но почему..."
    name_ii "Надо это проверить{w}, Юра положи карту на пол"
    th "Юра положил карту на пол{w}, а сами мы побежали в машину"

    scene bg ext_road_day with dissolve
    th "Юра и Влад уже спали{w}, а у нас с Сявой уже закрывались глаза"
    show blink
    th "Очередное затемнение"
    scene bg int_house_of_sl_day
    hide blink
    show unblink
    name_ura "ААААААААААААА"
    name_vladP "Да какого хуя ты всегда орёшь"
    name_vladM "Пацаны{w}, она лежит"
    th "Влад был прав{w}, карта была на полу"
    play music music_list['eat_some_trouble'] fadein 0.5
    name_vladP "АХУЕТЬ, АХАХАХХАХАХ"
    th "Мы были пиздецки рады{w}, хотя и в душе не ебали что с этим делать"
    name_vladP "Это единственная вещь, которая не поддаётся этой хуйне"
    name_vladM "Может нам надо уехать с ней?"
    name_ii "Не{w}, мы же в первый раз так и сделали"
    name_vladP "А что за крестик на ней?"
    th "На карте был изображён крестик, хотя по логике быть там его не должно"
    name_vladM "Так это даже не карта до Байкала{w}, это карта лагеря"
    name_ura "Нам нужно идти туда"
    stop music fadeout 0.5

    scene bg ext_house_of_sl_day with dissolve
    play sound sfx_open_dooor_campus_1
    play ambience ambience_camp_center_day fadein 0.5
    th "Мы вышли на улицу и отправились к месту которое помечалось крестом на карте"

    scene bg int_mine_exit_night_light with dissolve
    th "Через пару минут мы оказались у люка, который был укрыт листвой"
    name_ii "У меня ощущение, как будто нам туда"
    th "Сява руками смёл траву и листья в торону и первый начал лесть по лестнице вниз"
    th "Мы полезли вслед за ним"

    scene bg int_catacombs_entrance with dissolve
    stop ambience fadeout 0.5
    play ambience ambience_catacombs_stones fadein 0.5
    th "Перед нами оказался длинный тоннель, он как будто звал нас своей темнотой, из-за которой казался некончаемым"
    name_vladP "Ну потопали"
    name_vladM "Это либо у меня муражки{w}, либо здесь пиздецки холодно"
    name_ura "Это здесь холодно"

    scene bg int_mine_door with dissolve
    th "Тоннель оказался вовсе и не долгим{w}, пройдя по нему пару минут мы оказались у большой деревянной двери"
    name_vladM "И как нам это открыть?"
    name_ura "Ну в теории можно с разбега влететь в неё всем вместе"
    th "Мы отошли от стены на несколько метров и резко стартанули в сторону двери"
    th "Удара четверых взрослых чувачков хватило, что бы дверь улетела нахуй, понятное дело не прям на хуй, это фигура речи такая"

    scene bg int_mine_coalface with dissolve
    th "Перед нами открылась картина{w}, светящаяся пещера, которая как будто вела куда-то в иной мир"
    name_vladP "Мне кажется это оно"
    th "Разрывая коленки на штанах, мы ползли вперёд{w}, но тут ползущий вепереди Влад, резко упал на грудь"
    name_vladP "ВЛАД!{w} КАКОГО ХУ....."
    stop ambience fadeout 0.5
    show blink
    th "Темнота"
    scene bg int_house_of_sl_day
    hide blink
    show unblink
    name_ura "ААААААААААААААА"
    name_vladM "Да завали ты своё ебало"
    name_ii "Сссука{w}, нихуя не получилось"
    th "Лицо Влада казалось ещё более бледным чем обычно"
    name_vladM "Пойду покурю..."

    scene bg ext_house_of_sl_day with dissolve
    play sound sfx_open_dooor_campus_1
    th "Влад вышел на улицу и закурил{w}, бездонно смотря в пол"
    show dv normal pioneer with dissolve
    dv "Ооооо{w}, ебать вы поспать конечно пацаны{w}, и не кури здесь Влад{w}, Ольга увидит, пизды даст"
    th "Влад медленно повернул голову на Алису"
    dv "Что?"
    play music music_list['everlasting_summer'] fadein 0.5
    name_vladM "Сработало.....{w} СРАБОТАЛО МАТЬ ВАШУ!"
    show dv surprise pioneer with dspr
    dv "Что сработало?"

    scene bg int_house_of_sl_day with dissolve
    th "Влад залетел в домик"
    name_vladM "ПАЦАНЫ СРАБОТАЛО!{w} АЛИСА ЗНАЕТ НАС"
    name_vladP "Господи..."
    th "На душе стало так легко, как ещё никогда не было"
    name_ura "МЫ СПРАВИЛИСЬ БЛЯТЬ!"
    mt "Мальчики{w}, вы проснулись?{w} Можно войти?"
    name_ii "Входите"
    show mt normal pioneer with dissolve 
    mt "Я вам вчера не ту карту дала{w}, вот карта, которая до Байкала вас доведёт"
    name_vladP "*шёпотом* ты её тоже трахал Влад?"
    name_vladM "*шёпотом* раз восемь"
    name_ura "Спасибо огромное, ну нам пора"
    mt "Может сходите на завтрак"
    name_ii "НЕТ!{w} НАМ ПОРА"
    mt "Ну как хотите, пойдём{w}, мы вас проводим"

    scene bg ext_road_day with dissolve
    th "Уезжая я смотрел в зеркало заднего вида и видел девочек, которые махали нам вслед{w}, история кончено полный пиздец, но сейчас уезжая, даже как то не хотелось расставаться с ними{w}, но нас ждал Байкал...."
    stop music fadeout 0.5
    scene black with dissolve

    scene image_tachka with dissolve
    play music sound_carEdet fadein 0.5
    th "На большой скорости, дорога сливалась в одну большую полосу, а мелькающие за окном поля и леса, уже нихуёво так надоедали"
    name_ii "Блять{w}, как же я заебался{w}, кто нибудь может сменить меня?"
    th "В ответ была лишь тишина{w}, Юра и Влад спали на заднем сиденье, а я смотрел в окно, слушая музыку в наушниках"
    name_ii "Блять{w}, Влад...{w} ВЛАДИСЛАВ НАХУЙ!"
    th "Меня передёрнуло"
    name_vladP "Ааа{w}, чего тебе?"
    name_ii "Можешь меня сменить?"
    name_vladP "А ты не ахуел ли?{w} Едешь часа четыре только{w}, ещё два едь, а там поговорим"
    name_ii "Ну и иди в пизду"
    name_vladP "Хорошо"
    th "Выстроив на своём лице недовольство{w}, Сява продолжил вести тачку"
    name_vladM "Мгмх{w}, всем доброе"
    name_ii "Доброе"
    name_vladM "Чувак{w}, нам ещё долго ехать?"
    name_ii "Слушай{w}, я честно говоря хуй знает{w}, судя по карте мы едем в нужную сторону{w}, но когда мы точно приедем я понять не могу"
    name_vladP "Сява{w}, там какой-то водоём{w}, можешь стопнуть{w}, хочу умыться и горячего шоколада въебать"
    name_ii "Если остановлюсь, сменишь меня?"
    name_vladP "Да сменю, сменю, заебал"
    name_ii "Ура"
    stop music fadeout 0.5

    scene image_bereg with dissolve
    show image_vladM at right
    show image_vladP at fright
    with dissolve
    play music sound_rechka fadein 0.5
    th "Сява свернул к песчаному бережку у самой воды{w}, место было замечательное, вокруг не одного дерева"
    th "Мы с Владом вышли из тачки{w}, Сява же скрипя, перебрался на заднее сиденье"
    name_vladM "Аааагх{w}, как же хорошой, свежо!"
    name_vladP "Да не говори{w}, пить шайной дваколад на берегу{w}, звучит как мечта жизни"
    name_vladM "Ага"
    th "В такие моменты ощущаешь что-то пиздецки тёплое внутри{w}, когда стоишь на берегу воды, на песчаном пляже, в тысячах километров от дома, в компании главных дурачков в твоей жизни"
    th "Шоколад кончился"
    name_vladP "Бля{w}, руки зафаршмачил{w}, надо руки вымыть"
    th "Я подошёл к воде и окунул руки"
    name_vladP "Афагет{w}, вода холодная я его рот брал"
    name_vladM "Прям так?"
    name_vladP "Да"
    name_vladM "Так ладно{w}, пиздуй в тачку{w}, я поссу и приду"
    hide image_vladP with dissolve
    name_vladP "Ага"
    th "Влад вывалил своего чарончика и принялся ссать прям в воду"
    show image_digcaprio at left with dissolve
    chel "ЭЭЭЭ ПИЗДЮК!"
    name_vladM "Каво блять?"
    chel "Ты чё ахуел, пидрила?"
    name_vladM "А что не так то ебать?"
    chel "Ты блять ссышь в самое чистое озеро в России{w}, всё норм у тебя?"
    name_vladM "Чего нахуй?"
    chel "Блять это Байкал даун"
    name_vladM "Да?"
    chel "Ты ёбнутый?"
    name_vladM "ПАЦАНЫЫЫЫ! ЕБАААААТЬ! ВСЕ СЮДА!"
    th "Мы торкнули Юру, и вышли на берег"
    show image_vladP at fleft
    show image_ii
    show image_ura at cleft
    with dissolve
    name_ura "Че ты разорался придурок?"
    name_vladM "Мужики, это Байкал"
    name_vladP "Чего"
    name_vladM "ЭТО ОН НАХОООООЙ"
    name_ii "Блляяяя{w}, наконец-то приехали, слава богу..."
    name_vladP "А это чё за хуй?"
    chel "Ты чё ахуел?"
    name_vladM "Да всё мужик, пиздуй{w}, понял я, это Байкал{w}, больше в него ссать не буду"
    hide image_digcaprio with dissolve
    name_ura "А нахуй ты вообще в воду ссал?"
    name_vladM "Ну хочу я"
    name_vladP "Блять, а я центр-банк ограбить хочу, ну я же этого не делаю"
    name_vladM "А очень зря"
    name_ii "Так ну тогда поехали в Листвянку{w}, там ищем дом{w}, ииии..."
    name_vladM "ПИТЬ ПИВО"
    name_ii "Юхуууу"
    name_ura "Мда..."
    hide image_ii 
    hide image_vladM
    hide image_vladP
    hide image_ura
    with dissolve
    th "Мы сели в машину и действительно{w}, проехав по хуйне, перед нами открылся городок прям у огромного озера, вот оно - начало пиздатейших каникул"
    stop music fadeout 0.5

    scene image_list1 with dissolve
    play music sound_carEdet fadein 0.5
    th "Перед нами открылось удивительное место{w}, небольшой городок у берега одного из самых крутых водоёмов в мире"
    name_ii "Пацаны, это разъёб"
    name_vladP "Дааа{w}, прямо как в детстве"
    name_ura "Вау"
    th "Влад молчал{w}, он лишь с открытым ртом смотрел в окно"
    name_vladP "Мы же обещали свозить тебя на море, Сява."
    name_ura "Конечно не море{w}, но как по мне ни капли не хуже"
    name_ii "А у меня для вас сюрприз кстати"
    name_vladM "Сюрприз{w}, от СЯВЫ?"
    name_vladP "Ахуеть"
    name_ii "Я решил проблему с жильём и снял нам целый дом"
    name_ura "Чего нахуй?"
    name_ii "Я за неплохие деньги, продал код"
    name_vladP "Ебаааать{w}, смотри так и до собственной компании далеко"
    name_ii "Да не{w}, как бред звучит"
    stop music fadeout 0.5
    
    scene image_list2 with dissolve
    play music sound_listik fadein 0.5
    th "Мы захели в город{w}, туристы конечно были, но не так много как я себе представлял"
    name_vladM "Афагэт{w}, как же круто"
    name_ura "Сява{w}, а где домик то твой?"
    name_ii "Нужно проехать к концу города, по теории он там"
    th "В этом городке не было и намёка на многоэтажки{w}, все дома были максимум в 5 этажей и меньше{w}, но заметно много я увидел: ресторанов, кафе, баров."
    name_vladM "Сява{w}, омагад{w}, смотри, здесь везде бары"
    name_ii "Хахахах{w}, будет весело"
    th "Сам по себе городок не большой{w}, поэтому спустя несколько минут мы уже оказались на краю городка, у домика сявы"
    
    stop music fadeout 0.5
    scene image_domS with dissolve
    show image_ii at left
    show image_vladM at right
    show image_vladP at cright
    show image_ura
    with dissolve
    play music sound_domig fadein 0.5 
    name_ii "Ну вот это чудовище"
    name_ura "Ахуеть мужик, это же пиздец"
    name_ii "Да ладно{w}, я же не купил его{w}, а снял на полторы недели.."
    name_vladP "Так стоп..."
    name_vladM "Мы же на две недели приехали{w}, где мы будем оставшуюся половину недели"
    name_ii "Честно не ебу{w}, денег только на столько хватило"
    name_ura "Ладно{w}, гостиницу снимем или на край в палатке затусуемся"
    name_vladM "Я твою палатку рот долбил{w}, сам в ней спи"
    name_ura "Иди-ка ты в хуй, гэй"
    name_vladM "Писю в попу запихини"
    name_ii "Влад.."
    name_vladP "А?"
    name_ii "Пусть эти тут себе что-нибудь куда-нибудь пихают{w}, а мы пойдём заселяться"
    name_vladP "Ле го"
    th "Мы зашли во внутрь"
    stop music fadeout 0.5

    scene image_gostin with dissolve
    show image_ii
    show image_vladP at right
    with dissolve
    play music sound_classikmzk fadein 0.5
    name_vladP "Пиздец харомы брат"
    name_ii "Я на сайте видел огромные виллы, но это то, на что денег хватило"
    name_vladP "Да чувак это разъёб{w}, не ожидал от тебя"
    name_ii "Я от себя тоже"
    th "Вошли Влад и Юра"
    show image_ura at left
    show image_vladM at fleft
    with dissolve
    name_vladM "Ёбаный конь{w}, что за хата"
    name_ura "Что тебе сделал конь?"
    name_vladM "Игогокнул"
    name_ii "Кароч{w}, только тут проблемка есть"
    name_vladP "Блять ну конечно{w}, я так и думал"
    name_ii "Да не{w}, всё норм{w}, просто тут всего две спальни"
    name_ura "Ага.{w} А другие комнаты это что?"
    name_ii "Сауна{w}, кухня{w}, библиотека"
    name_vladM "Ты взял дом с библиотекой?{w} На тебя не похоже"
    name_ii "Пошёл в пизду"
    name_ura "Так{w}, ну значит вы в троём в одной спальне, а я в другой"
    name_vladP "Оближи и проглоти"
    name_ura "Не ну а чё"
    name_ii "Так{w}, кароч{w}, с юрой будет жить Влад{w}, тот что тупой"
    name_vladP "Бля"
    name_vladM "Бля"
    name_ura "Ты про кого из двоих?"
    name_ii "Про обоих{w}, вот они два Влада, пусть вместе и живут"
    name_vladM "Оооо{w}, пижамная вечеринка Владов"
    name_vladP "Других не пускаем"
    name_vladM "Будем пить вино и обсуждать мальчиков"
    name_vladP "Да{w}, хихихих"
    hide image_ii 
    hide image_vladM
    hide image_vladP
    hide image_ura
    with dissolve
    th "Мы начали расходиться{w}, я и Влад заняли комнату на втором этаже{w}, а Юржи и Слейвс потопали в комнату которая была на первом, прямо под нашей"
    show image_ii at right
    show image_vladP 
    show image_ura at fleft
    show image_vladM at left
    with dissolve
    th "Через час разбора вещей, мы встретились в гостинной"
    name_ura "Так{w}, предлагаю сначала пойти покушать в кафе{w}, а потом можно уже и разгуляться"
    name_ii "Согласен"
    th "Мы вышли на улицу и потопали в глубь города"
    stop music fadeout 0.5

    scene image_ahye with dissolve
    show image_ii at left
    show image_vladP at right
    show image_ura 
    show image_vladM at fleft
    with dissolve
    play music sound_listik fadein 0.5
    name_vladP "Афагэт{w}, как же много тут всякого"
    name_ii "Давайте сюда залетим"
    th "Сява указал на летнюю кафешку с шатром{w}, имеющую название \"Ах, у Эли\""
    name_ura "Хахах{w}, интересное название{w}, ну погнали"
    stop music fadeout 0.5
    
    scene image_cafev with dissolve
    show image_ii at right
    show image_vladP 
    show image_ura at fleft
    show image_vladM at left
    with dissolve
    play music sound_obozekakoi fadein 0.5
    th "Вот мы оказались внутри и сели за первый попавшийся столик{w}, самое смешное что мы были единственными в этом кафе"
    name_ura "Ну сразу видно{w}, место популярное пиздец"
    th "К нам подошёл официант"
    show image_oficnegr at fright with dissolve
    offnik "Здравствуйте{w}, меня зовут Андрей, сегодня я ваш официант{w}, что хотите заказать"
    name_vladM "Привяу{w}, кароч, мне сочный бургер, картошку среднюю и колу"
    offnik "Хорошо{w}, вам хлеб нужен?"
    name_vladM "Да{w}, чёрный можно...{w}а у вас случаем твикса нет?"
    offnik "Есть{w}, желаете?"
    name_vladM "Да{w}, несите"
    name_ura "Мне пожалуйста салат цезарь и порцию шашлыка{w}, ну и колу давате"
    name_vladP "Я бы не отказался от трёх куриных ножек и порции картошки фри{w}, из напитков хочу шоколадный милкшейк"
    name_ii "А мне пожалуйста маленькую пиццу, картошку и Фанту пожалуйста"
    offnik "Ваши заказы приняты{w}, в течении двадцати минут ожидайте"
    hide image_oficnegr with dissolve
    name_vladP "Наконец-то нормальная блять еда{w}, а то от дошика уже тошнит"
    name_ura "Да не говори"
    name_ii "Чуваки{w}, думаю это будут лучшие каникулы в нашей жизни"
    name_vladM "Ураааа"
    show image_sp20min with dissolve
    $ renpy.pause(3)
    hide image_sp20min with dissolve
    show image_oficnegr at fright with dissolve
    offnik "Прошу{w}, ваш большой заказ"
    hide image_oficnegr with dissolve
    name_ura "Спасибо большое{w}, ну что чувачьё{w}, налетаем"
    th "Плтоно наевшись{w}, мы вышли на улицу"
    stop music fadeout 0.5
    
    scene image_ylisa with dissolve
    show image_ii at fleft
    show image_vladP at right
    show image_ura at left
    show image_vladM 
    with dissolve
    play music sound_listik fadein 0.5
    name_vladP "Так{w}, как гвориться{w}, плотно поев надо плотно наебениться"
    name_ura "Кто так говорит?"
    name_vladP "Теперь я"
    th "Буквально на этой улицы стоял бар из которого громко играла музыка"
    stop music fadeout 0.5
    
    show image_barr with dissolve
    show image_ii 
    show image_vladP at left
    show image_ura at right
    show image_vladM at fleft
    with dissolve
    play music sound_govno fadein 0.5
    name_vladM "Нормальное местечко{w}, ещё бы музыка нормальная играла{w}, то вообще бы заебись было"
    name_ura "Да сойдёт"
    th "Усевшись за столик{w}, я принялся толкать речь"
    name_vladP "Итак{w}, пацаны и пацанессы{w}, хочу поднять этот стакан за то{w}, что бы эти канкулы прошли ахуенно и больше без каких либо происшествий"
    name_ii "Да{w}, думаю уже ничего плохого произойти не должно"
    th "Мы принялись глушить стакан за стаканом{w}, и я не заметил как сознание полностью покаинуло меня"
    stop music fadeout 0.5
    show blink
    th "Где я?"
    th "Это рай?{w} Может ад?"
    th "Вокруг была лишь беспросветная тьма и ничего больше"
    th "Может я набухался и умер?"
    th "Ну пиздец{w}, у меня же там родители, брат, друзья остались{w}, а я так просто умер"
    play music sound_proboi fadein 0.5
    th "Почему то в этой темноте я слышал звук прибоя"
    th "Наверно так выглядит смерть{w}, но почему прибой?"
    hide blink
    show unblink

    scene image_loda1 with dissolve
    show image_vladP
    show image_ura at left
    show image_vladM at right
    with dissolve
    th "Резко тьма стала растворяться"
    name_vladP "ЭЭээээгх{w}, кх кх"
    name_vladP "Какого хуя?"
    th "Передо мной была картина{w}, обычная деревянная лодка в которой лежал я, Юра и Влад"
    th "Я бы подумал что мы уплыли в бескрайний океан{w}, но нет, лодка была прибита к берегу{w}, берег, слава богу, Байкала"
    name_vladP "Чуваки{w}, чувакииии"
    name_ura "Бргхм{w}, аааааа"
    name_vladM "Влад иди нахуй{w}, тебе ещё час ехать"
    name_vladP "Мужики вставайте{w}, что мы в лодке делаем?"
    name_ura "Аггх{w}, ну поплавать решили"
    name_vladP "ВЛАД ВСТАЛ НАХУЙ!"
    th "Я стукнул Влада по макушке"
    name_vladM "Ты плохой человек"
    name_vladP "Где Сява?"
    th "Я осмотрел лодку вокруг и никого не нашёл"
    th "Тут раздался крик"
    name_ura "Аааааааа{w}, бляяяять"
    name_vladM "Что ты орёшь{w} и так голова болит"
    th "К Юриной руке была привязана цепь на обратной стороне которой сидела маленькая обезянка"
    name_vladP "Вот тебе нахуй{w}, откуда это животное взялось?"
    name_ura "Я НЕ ЕБУ МУЖИК{w}, МЫ ЧЁ ОБЕЗЬЯНУ КУПИЛИ?"
    name_vladM "Так, разберёмся{w}, надо Сяву искать"
    th "Юра взял обезьяну на руки и мы вылезли из лодки"
    name_vladP "Так все проверьте, доки у всех с собой?"
    name_ura "У меня всё на месте"
    name_vladM "У меня тоже{w}, стоп......{w}чего?"
    th "Влад открыл свой паспорт"
    name_vladP "Что такое?"
    name_vladM "ЧУВАКИ БЛЯТЬ!"
    th "Влад развернул паспорт в нашу сторону{w}, страница с семейным положением была заполнена"
    name_vladM "Я ЖЕНАТ НАХУЙ!"
    name_ura "Сука{w}, чего вообще было вчера?{w} Где Сява?{w} Я нихуя не понимаю"
    name_vladM "БЛЯТЬ Я ЖЕНАТ ЧУВАКИ{w}, КАКОГО ХУЯ А?"
    name_vladP "Блять{w}, ебало на куски разрывается{w},думаю надо первым делать сходить в тот бар"
    name_ura "Да{w}, хорошая идея"
    name_vladP "Тогда погнали"
    th "От каждого шага хотелось ёбнуться на землю{w}, голова куржилась, ещё и жёсткое похмелье ебало мозг"
    th "Пройдя чуть чуть, мы оказались в баре"
    stop music fadeout 0.5

    scene image_barr with dissolve
    show image_vladP
    show image_ura at cright
    show image_vladM at right
    show image_oficnegr at left
    with dissolve
    name_ura "Здравствуйте"
    offnik "Ну привет молодёж"
    name_vladP "Вы здесь официантом работаете?"
    offnik "Да{w}, город маленький, много свободных вакансий"
    name_vladP "Ладно, не столь важно"
    name_vladP "Вы нас помните?"
    offnik "Ну конечно!{w} Давно у нас не было таких клиентов"
    name_vladM "У нас память отшибло к ебеням{w}, вы не знаете ли{w}, куда мы отправились после нашего феерического бухича?"
    offnik "Я не уверен{w}, но когда вас унесло с концами{w}, тот что с портфелем и высоких начал громко орать, что-то вроде \"ХОЧУ ШЛЮХ ТРАХАТЬ, ПОЕХАЛИИИИ\""
    name_vladP "Ну это точно Сява"
    name_ura "Значит на этом этапе он был с нами"
    name_vladM "Простите за нескромный вопрос{w}, а где у вас тут шлюхи?"
    offnik "Дальше по улице{w}, и направо, там переулок"
    name_ura "Спасибо"
    th "Мы отправились к шлюхам"

    scene image_pereyl with dissolve
    show image_vladP
    show image_vladM at cright
    show image_ura at right
    with dissolve
    play music sound_ytro fadein 0.5
    name_vladP "Ээээ{w}, здравствуйте"
    name_ura "Здесь есть кто-нибудь?"
    show image_gena at left with dissolve
    gena "Аааа{w}, любимый{w}, я же сказала, как закончу на работе, приеду"
    th "Резко выбежавшая девушка, влетела во Влада и начала его обнимать"
    name_vladM "Девушка{w}, вы кто?"
    gena "Зай{w}, ты чего?"
    name_vladM "Сука{w}, да я реально тебя не знаю, вы меня с кем-то перепутали"
    name_ura "Влад{w}, я кажется понял{w}, девушка, вы не могли бы показать графу семейного положения в паспорте"
    gena "Да, конечно"
    th "Она достала из кармана пасопрт, и открыла страницу с семейным положением, Юрина догадка оказалась правдой"
    name_ura "Знакомься Влад{w}, твоя жена"
    name_vladM "Блять{w}, это пиздец"
    name_vladP "Девушка{w}, у нас вчера был жёсткий забух{w}, вы не могли бы рассказать что вчера здесь было?"
    gena "Ну вы вчера приехали{w}, с вами ещё был один парень, он кричал что хочет шлюху, все дела"
    name_ura "Ну пока звучит обычно{w}, но как так вышло что ты замужем за нашего друга"
    gena "Ну он снял меня{w}, но вместо секса, начал рассказывать о своей жизни{w}, а позже и вовсе стал признаваться мне в любви{w}, а ещё через пятднадцать минут сделал мне предложение"
    name_vladM "И ты так просто согласилась?"
    gena "Ну да{w}, ты был такой искренний"
    name_vladP "Так{w}, сейчас это не столь важно{w}, ты не знаешь, куда мы отправились потом?"
    gena "Честно{w}, незнаю{w}, вы куда-то ушли, а я с милым уехали в загс"
    name_vladP "Так{w}, значит уезжая от сюда, Сява всё ещё был с нами"
    name_ura "Угу{w}, но вот вопрос, куда мы поехали потом"
    name_vladM "Ну моё предположение{w}, что позже мы поехали туда, где ты, Юра, добыл обезьяну"
    th "И правда{w}, всё это время Юра продолжал держать при себе маленькую обезянку на цепочке"
    name_ura "Слушай{w}, зовут тебя как?"
    gena "Агафья"
    name_ura "Агафья{w}, где в этом городе можно теоритически было взять обезьяну"
    gena "Ну варика два{w}, зоопарк или приезжий цирк"
    gena "Но вот только зоопарк строго охраняется и вы при большом желании, в таком состоянии, даже бы не подошли к входу"
    name_vladP "Так{w}, ну значит идём к цирку"

    scene image_cirk with dissolve
    th "Не долго топая, мы оказались у огромного шатра"
    name_vladP "По теории, внутри некого{w}, сегодня у них выходной"

    scene image_cirkv with dissolve
    show image_vladP at cright
    show image_ura 
    show image_vladM at right
    with dissolve
    th "Мы зашли во внутрь"
    name_ura "Алооу{w}, здесь есть кто-нибудь"
    name_vladP "Тут никого нет{w}, то есть мы просто пришли и спизидили обезьяну?"
    name_vladM "Судя по всему да"
    name_ura "Блять{w}, мы удивительные идиоты"
    name_vladP "Блять это тупик{w}, дальше нет проводников"
    name_ura "Вопрос, где и в какой момент мы проебали Сяву"

    scene image_cirk with dissolve
    show image_vladP 
    show image_ura at left
    show image_vladM at cleft
    with dissolve
    th "Мы вышли на улицу"
    show image_bomj at right with dissolve
    bomg "Егхехе{w}, удивительно что вы ещё живы?"
    name_vladP "Чего нахуй?{w} Чё те надо алкаш?"
    bomg "Ну вчера же до вас докопались те наркоманы"
    name_ura "Какие нахуй наркоманы дед?"
    bomg "Ну у нашего городка есть проблема{w}, в городеесть групка наркоманов, да к тому же они ещё и сатанисты{w}, ходит слушок что у них где-то есть место где они творят какие-то ужасные вещи"
    name_vladM "Ахуеть{w}, а мы тут причём?{w} Что они нам вчера говорили"
    bomg "А вы что{w}, не помните ничего?"
    name_vladP "БЛЯТЬ НЕТ!{w} ВОТ ИМЕННО!{w} МЫ НИХУЯ НЕ ПОМНИМ ДЕД-ПЕРДЕД"
    bomg "Ну вы вышли из шотра с обезьяной и к вам подошли эти парни"
    name_vladP "Так{w}, ну а потом?"
    bomg "Они предложили что бы вы отдали им обезьяну для всяких их штучек"
    name_vladM "Так{w}, ну обезьяна у нас"
    bomg "Ну они уходили с каким то парнем"
    name_vladM "Так стоп...."
    name_ura "Блять..."
    name_vladP "Твою мать{w}, мы кажется им отдали Сяву, вместо обезьяны"
    bomg "Ахуенные вы друзья"
    name_ura "А сосни ка хуйца старый"
    th "Мысль не укладывалась в голове{w}, как мы могли оставить обезяну, но при этом отдать им Сяву"
    name_vladP "Сука{w} СУКА{w} ГДЕ НАМ ТЕПЕРЬ ЕГО ИСКАТЬ?{w} ОН ВООБЩЕ ЖИВ?"
    name_ura "Так{w}, вспоминаем{w}, куда теоритически его могли увести"
    name_vladM "ДА ОТКУДА МЫ ЕБЁМ{w}, МЫ ЗДЕСЬ ОДИН БЛЯДСКИЙ ДЕНЬ"
    name_vladP "Я кажется понял"
    name_ura "А?"
    name_vladP "Мы хотели вернуть Сяву{w}, но вырубились"
    name_vladM "Так{w}, и что?"
    name_vladP "А где мы проснулись?"
    name_ura "Ааааа{w}, думаешь он на том берегу?"
    name_vladP "Думаю да"
    name_vladM "Тогда погнали"
    stop music fadeout 0.5

    scene image_loda1 with dissolve
    play music sound_proboi fadein 0.5
    th "За пару минут мы уже стояли на каменном пляже{w}, у той самой лодки"
    name_ura "Толкайте её в воду"
    
    scene image_loda2 with dissolve
    th "Еле как сдвинув её с места и перерезав канат{w}, мы отчалили"
    th "Грести вёслами оказалось энергозатратней чем мы предпологали{w}, поэтому путь занял минут сорок, но мы наконец-то приплыли"
    stop music fadeout 0.5

    scene image_izba1 with dissolve 
    show image_vladP at right
    show image_ura at cright
    show image_vladM 
    with dissolve
    
    name_vladP "Блять{w}, тут так жутко"
    name_ura "Смотрите{w}, избушка"
    th "Мы очень тихо подошли к ней{w}, стараясь не шуметь хрустом веток и листиков"
    th "Только я хотел обсудить план{w}, как вдруг Влад с палкой в руке влетел внутpь здания"

    scene image_izba2 with dissolve
    show image_vladP at cright
    show image_ura 
    show image_vladM at right
    show image_ii at fleft
    show image_jonisini at left
    with dissolve
    name_vladM "ВСЕМ НАХУЙ ОСТАВАТЬСЯ НА МЕСТАХ{w}, А ИНАЧЕ ВСЕХ К ХУЯМ ПЕРЕЕБАШУ"
    th "Картина была до пизды ужасающая{w}, на столу лежал Сява, который был живой{w}, но спал{w}, а перед ним стояли три голых парня{w}, они все были измазаны какими-то красками, а в руках у них были охапки трав, которые тлели и пепел ссыпался прям на сяву"
    name_vladM "Мать моя женщина...."
    hide image_jonisini with dspr
    th "Точно не помню что в тот момент произошло{w}, но спустя буквально пару мгновений парни лежали на полу{w}, а Влад с бешеным взглядом смотрел на них{w}, держа в руке окрававленную палку........{w}чёрный импульс?" with hpunch
    name_ura "А ты хорош мужик"
    show blink 
    scene image_barr
    show image_vladP at left
    show image_ura at cright
    show image_vladM 
    show image_ii at right
    $ renpy.pause(3)
    hide blink
    show unblink
    name_ii "История звучит как полный бред{w}, вы меня точно не разыгрываете?"
    name_ura "Ты думаешь мы бы выдумали такое?"
    name_ii "Где тогда обезьяна?"
    name_ura "Я отдал её тому бомжу{w}, он теперь деньги с помощью неё лутает"
    name_ii "А как же жена Влада?"
    th "Влад открыл паспорт"
    name_vladM "Впитывай{w}, съездили, развелись"
    name_ii "А те парни?"
    name_vladP "Они оказывается здесь знаменитости, но никому никогда реального вреда не причинили{w}, ты же по факту добровольно с ними пошёл"
    name_ii "Блять{w}, незнаю как вы{w}, но я точно до конца каникул пить не собираюсь......{w} может быть"



label ne_vipil_tabletki:
        