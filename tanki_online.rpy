init:

    $ mods ["doroga"] = u"tanki_online"

#region image
    
#endregion


#region sound

#endregion


#region name
    $ vladM   = Character (u'ВладМ', color = "#60ca3f", what_color = "#FFFFFF")
    $ vladP   = Character (u'ВладП', color = "#76d4ff", what_color = "#FFFFFF")
    $ ura     = Character (u'Юра',   color = "#FF8C00", what_color = "#FFFFFF")
    $ siava   = Character (u'Сява',  color = "#cc5233", what_color = "#FFFFFF")

#endregion

    transform begg:
        zoom 1.05 anchor (48, 27)
        ease 0.10 pos (0,0)
        ease 0.10 pos (25, 25)
        ease 0.10 pos (0, 0)
        ease 0.10 pos (-25, 25)
    repeat

label doroga: