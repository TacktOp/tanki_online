init:

    $ mods ["doroga"] = u"tanki_online"

#region image
    image image_vladM     = "image/владпнг.png"
    image image_ii        = "image/сявапнг.png"
    image image_ura       = "image/Юрапнг.png"
    image image_vladP     = "image/япнг.png"
    image image_cardoroga = "image/машина едем.jpg"
    image image_DvladM = "image/владк.png"
    image image_Dii = "image/сявак.png"
    image image_Dura = "image/юрак.png"
    image image_DvladP = "image/япнгк.png"

#endregion


#region sound
    $ sound_ = ""
#endregion


#region name
    $ name_vladM   = Character (u'ВладМ',  color = "#60ca3f",   what_color = "#FFFFFF")
    $ name_vladP   = Character (u'ВладП',  color = "#76d4ff",   what_color = "#FFFFFF")
    $ name_ura     = Character (u'Юра',    color = "#FF8C00",   what_color = "#FFFFFF")
    $ name_ii      = Character (u'Сява',   color = "#cc5233",   what_color = "#FFFFFF")
    $ name_rem     = Character (u'Рем',    color = "#00a2ff",   what_color = "#FFFFFF")
    $ name_matvei  = Character (u'Матвей', color = "#1e7055ff", what_color = "#FFFFFF")

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
    name_ura "Сява, поставь воду кипятиться."
    name_ii "Ща оформлю."
    th "Мы расстелили около подсолнухов большой плед и разложили на нем дошики и хлеб."
    name_ii "Может буданём алкаша, что бы тоже поел."
    name_ura "Да ненадо{w}, пусть спит."
    name_vladP "Кста, че у тебя по практике Юра?"
    name_ura "Да эти мудаки захотели меня засунуть к старшим классам, я отказался."
    name_ii "Че так?"
    name_ura "Да они тупые как пробки, особенно девочки{w}, вроде оддинадцатый класс, а одеваются как шалавы."
    name_vladP "Хахахах{w}, ну так бомби, подцепишь какую-нибудь там."
    name_ura "Ты даун?{w} Я не настолько конченый{w}, да и в тюрьму я не хочу.{w} Да и камон{w}, это же всё ещё дети."
    name_ii "Ну поживём увидем."
    name_ura "Иди-ка нахуй."
    name_vladP "Хахахха{w}, ладно, погнали уже."
    th "На ходу допив жижку от говяжего дошика, я упал на переднее сиденье, а Юра кряхтя уселся за руль."
    th "Не успели мы проехать и километра{w}, как мы услышали посапывание Сявы, который наевся и спит."
    th "Вот погода опять начала хериться{w}, и палящая жара сменилась приятной свежестью."
    name_vladP "Чувак, сам проедешь?{w} А то меня в сон клонит, вздремнуть бы по хуйне."
    name_ura "Да всё оки{w}, спи."
    th "Я заснул сразу же как закрыл глаза."
    th "Пока мы все спали, Юра двигался по узкой дороге без асфальта, которая проходила прям в чаще леса."
    th "Он взглянул на время{w}, было пол пятого."
    name_ura "Блять{w}, таблетки же нужно выпить{w}.... сука они в багажнике, это надо блять останавливаться ещё."
    name_ura "А может в пизду{w}, потом выпью{w}, хмм."
