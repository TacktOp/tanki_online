init:

    $ mods ["doroga"] = u"tanki_online"

#region image
    image image_vladM     = "image/владпнг.png"
    image image_ii        = "image/сявапнг.png"
    image image_ura       = "image/Юрапнг.png"
    image image_vladP     = "image/япнг.png"
    image image_cardoroga = "image/машина едем.jpg"

#endregion


#region sound
    $ sound_ = ""
#endregion


#region name
    $ name_vladM   = Character (u'ВладМ',  color = "#60ca3f", what_color = "#FFFFFF")
    $ name_vladP   = Character (u'ВладП',  color = "#76d4ff", what_color = "#FFFFFF")
    $ name_ura     = Character (u'Юра',    color = "#FF8C00", what_color = "#FFFFFF")
    $ name_siava   = Character (u'Сява',   color = "#cc5233", what_color = "#FFFFFF")
    $ name_rem     = Character (u'Рем',    color = "#00a2ff", what_color = "#FFFFFF")
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
