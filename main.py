import pygame  # impordime pygame mooduli
import random  # impordime random mooduli

pygame.init()  # käivitame pygame

# ekraani seaded
ekraanX, ekraanY = 640, 480  # määrame ekraani suuruse muutujad
ekraan = pygame.display.set_mode([ekraanX, ekraanY])  # määrame ekraani suuruse (väärtused muutujatest) ja omistame muutujasse ekraan
pygame.display.set_caption("Ülesanne 6: Korrastada mäng Ping-Pong")  # määrame ekraanie pealkirja
ekraani_varv = [99, 99, 99]  # määrame ekraani tasutavärvi muutujasse
ekraan.fill(ekraani_varv)  # täidame ekraani taustavärviga
FPS = pygame.time.Clock()  # loome FPS muutuja ja omistame pygame kella väärtuse

# heli
pygame.mixer.music.load('heli/taustamuusika.mp3')  # laadime helifaili
pygame.mixer.music.play(-1)  # määrame helifaili lõpmatult kordama
pygame.mixer.music.set_volume(0.2)  # määrame heli tugevus

# palli seadistamine (suurus, kiirus, asukoht)
pall_X, pall_Y = random.randint(100, 600), random.randint(100, 300)  # määrame palli kordinaadid
pall = pygame.Rect(pall_X, pall_Y, 20, 20)  # määrame palli suuruse muutujasse
pall_pilt = pygame.image.load("pildi_failid/pall.png")  # laeme palli pildi muutujasse
pall_pilt = pygame.transform.scale(pall_pilt, [pall.width, pall.height])  # määrame palli pildi suuruse
pall_kiirus_X, pall_kiirus_Y = 5, 7  # määrame palli kiirused muutujad vastavatel telgedel

# aluse seadistamine (suurus, kiirus, asukoht, suuna muutuja)
alus_X, alus_Y = 260, ekraanY - 100  # määrame alus kordinaadid
alus = pygame.Rect(alus_X, alus_Y, 120, 20)  # määrame aluse suuruse muutujasse
alus_pilt = pygame.image.load("pildi_failid/alus.png")  # laeme aluse pildi muutujasse
alus_pilt = pygame.transform.scale(alus_pilt, [alus.width, alus.height])  # määrame aluse suuruse
aluse_suund = 0  # määrame aluse suuna muutuja
alus_kiirus = 9  # määrame aluse likumis kiiruse muutuja

# teksti font ja skoor
font = pygame.font.Font(pygame.font.match_font('Arial'), 25)  # määrame muutujale "font" suuruseks 25 ja fondiks "Arial"
skoor = 0  # punktiarvestuse muutuja

while True:  # nii kaua, kui tsükkel on tõene,

    FPS.tick(60)  # värskendame ekraani 60 korda sekundis
    alus = pygame.Rect(alus_X, alus_Y, 120, 20)  # määrame aluse suuruse ja kordinaadid muutujasse
    pall = pygame.Rect(pall_X, pall_Y, 20, 20)  # määrame palli suuruse ja kordinaadid muutujasse
    tekst = font.render("Skoor: " + str(skoor), True, [255, 255, 255])  # omistame muutujale tekst väärtuseks sõne ja muutujast skooroleva arvu ja värvime selle valgeks
    pall_X -= pall_kiirus_X  # muutujalt pall_X lahutatakse pall_kiirus_X väärtus
    pall_Y -= pall_kiirus_Y  # muutujalt pall_Y lahutatakse pall_kiirus_Y väärtus

    for syndmus in pygame.event.get():  # sükkli muutujale omistatakse kõik pygame.event.get() väärtused

        if syndmus.type == pygame.QUIT:  # kui tsüklimuutuja syndmus tüüp võrdub pygame.QUIT
            pygame.quit()  # sulgeme pygame
            exit()  # lõpetame programmi

        # klahvi vajutus
        if syndmus.type == pygame.KEYDOWN:  # kui sündmuse tüüp on klahvi vajutus, siis
            if syndmus.key == pygame.K_RIGHT:  # kui sündmuse klahv on parem noole klahv, siis
                aluse_suund = "parem"  # muutujale aluse_suund omistatakse väärtuseks võne "parem"
            elif syndmus.key == pygame.K_LEFT:  # kui sündmuse klahv on vasak noole klahv, siis
                aluse_suund = "vasak"  # muutujale aluse_suund omistatakse väärtuseks võne "vasak"

        # klahvi lahti laskmine
        if syndmus.type == pygame.KEYUP:  # kui sündmuse tüüp on klahvi lahti laskmine, siis
            if syndmus.key == pygame.K_RIGHT or syndmus.key == pygame.K_LEFT:  # kui vasak või parem noole klahv on lahti lastud, siis
                aluse_suund = 0  # muutujale aluse_suund omistatakse väärtuseks 0

    # aluse liigutamine klaviatuuriga
    if aluse_suund == "vasak":  # kui muutuja aluse_suund võrdub sõnega vasak, siis
        if alus_X > 0:  # kui alus_X on suurem kui 0, siis
            alus_X -= alus_kiirus  # muutujale alus_X lahutatakse muutuja alus_kiirus väärtus
    elif aluse_suund == "parem":  # kui muutuja aluse_suund võrdub sõnega parem, siis
        if alus_X + alus_pilt.get_rect().width < ekraanX:  # kui alus_X, millele on liidetud aluse laius on väiksem kui, muutuja ekraanX, siis
            alus_X += alus_kiirus  # muutujale alus_X liidetakse muutuja alus_kiirus väärtus

    # palli liikumine
    if pall.colliderect(alus) and pall_kiirus_Y < 0:  # Kui palli ja aluse vahel toimub kokkupõrge ja palli Y suund on väiksem kui 0
        skoor += 1  # lisame muutujale skoor +1
        pall_kiirus_Y = -pall_kiirus_Y  # muudame palli suunda (muudame palli y kiiruse/kordinaadi muutuja vastandarvuks)
    if pall_X > ekraanX - pall_pilt.get_rect().width or pall_X < 0:  # kui palli x kordinaat on suurem kui ekraani oma ja väiksem kui 0, siis
        pall_kiirus_X = -pall_kiirus_X  # muudame palli suunda (muudame palli x kiiruse/kordinaadi muutuja vastand arvuks)
    if pall_Y > ekraanY - pall_pilt.get_rect().width or pall_Y < 0:  # kui palli y kordinaat on suurem kui ekraani oma ja väiksem kui 0, siis
        pall_kiirus_Y = -pall_kiirus_Y  # muudame palli suunda (muudame palli y kiiruse/kordinaadi muutuja vastandarvuks)

    # ekraanil asjade kuvamine
    ekraan.fill(ekraani_varv)  # täidame ekraani taustavärviga
    ekraan.blit(pall_pilt, pall)  # kuvame ekraanil palli
    ekraan.blit(alus_pilt, alus)  # kuvame ekraanil alust
    ekraan.blit(tekst, [500, 50])  # kuvame ekraanil muutuja tekst väärtuse kordinaatidega 520,20
    pygame.display.flip()  # värskendame tervet ekraani

    if pall_Y > ekraanY-pall_pilt.get_rect().height:  # kui pall_y väärtus on suurem, kui muutuja ekraanY millelt on lahutatud palli kõrgus, siis
        pygame.quit()  # sulgeme pygame
        exit()  # lõpetame programmi
