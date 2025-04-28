# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[McName]")
define unk = Character("???")

default eksplor = 0
default ngobrolBundaran = 0
default ngobrolKantin = 0
default ngobrolMasjid = 0
default ngobrolLp2 = 0
default ngobrol_r101 = 0
default ngobrol_r106 = 0
default ngobrol_r109 = 0
default places_discovered = {
    gedung1 = False
    gedung2 = False
    kantin = False
    r101 = False
    r106 = False
    r109 = False
    lt2 = False
    lt3 = False
    lp2 = False
    masjid = False
    parkiran = False
    aula = False
    tu = False
    lt2_closed = False
}
init python:
    def discovered_all_places:
        return all(places_discovered.values())

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    unk "Hey... Kamu"

    unk "Ya, Aku bicara denganmu"

    unk "Siapa namamu?"

    $ McName = renpy.input("Siapa Namamu?", default = "Sopo")
    $ McName = McName.strip()

    unk "[McName] ya, Salam kenal. Namaku adalah &%%^E*%%$*$%%$^&*%%$#"

    unk "Aku dengar kamu ingin memainkan game ini karena kamu ingin kuliah di ITS,
    atau kamu hanya ingin sekedar bermain?"

    unk "Apapun alasanmu aku tidak akan berkomentar."

    unk "Jika kamu adalah orang yang ingin masuk ke ITS dengan jalur SNBT..."

    unk "Ingatlah kunci agar lulus SNBT itu adalah......."

    hide eileen happy

    jump prologue

    # This ends the game.
    # return

label prologue:

    mc "Uwahhhhh!!!!!"

    mc "huft... huft...."

    mc "Mimpi apa itu tadi?"

    mc "Ah daripada mikirin mimpi, mending aku lanjut cari jurusan yang cocok"

    "Sudah berapa hari semenjak aku gagal lolos SNBP?"

    "Aku benar benar tidak tahu harus mengambil jurusan apa saat kuliah nanti"

    "Tetapi aku harus tetap mencari"

    "Aku tidak ingin hanya menjadi beban bagi orang tuaku"

    "Sudah saatnya aku mencari jurusan yang dapat mengubah hidupku yang biasa-biasa ini"

    mc "Hmm... jurusan yang dapat mengubah hidup ya..."

    "Aku membuka browser di laptopku dan mulai mencari jurusan yang relate denganku"

    mc "Mari kulihat... Jurusan dengan gaji lulusan tertinggi"

    mc "Kedokteran.... ah aku ngga suka biologi."

    mc "Akuntansi.... kurang suka juga sama ekonomi"

    mc "Teknik Elektro..... agak bingung juga dengan kelistrikan"

    mc "Teknik Informatika..... hmm?"

    mc "Wah boleh banget sih ini, mumpung aku punya pengalaman ngecheat di game juga"

    mc "Sekarang nyari kampusnya..."

    mc "Oh ITS di dalam kota juga ternyata"

    mc "Mantap nih ga perlu bingung ngekos"

    mc "Tapi kampus ini bagus kah?"

    "Sesaat setelah aku mengeluarkan kata-kata itu..."

    "Rasanya ingin aku tarik balik."

    mc "!!!"

    mc "Ada yang lolos informatika ITS nilai SNBT nya paling tinggi di 2023???"

    mc "Buset bukan kampus kaleng kaleng sih inimah kalo yang pengen masuk aja nilainya paling tinggi gitu."

    mc "Hmmm... tapi kalo yang lolos dengan nilai segitu, berarti pasti banyak juga yang ingin masuk ke jurusan ini di ITS."

    mc "Kalo gitu aku harus lebih giat belajar lagi biar keinginanku bisa kecapai."

    "Satu bulan telah berlalu, aku tidak pernah berhenti untuk belajar dan mencoba semua try out SNBT yang
    dapat aku temukan."

    "Walaupun nilai SNBT yang keluar masih belum memenuhi targetku, aku tidak ingin menyerah begitu saja. 
    Apapun yang terjadi aku harus lolos ke jurusan ini."

    "Sebentar tetapi aku sepertinya melupakan sesuatu...."

    mc "EH IYA AKU BELUM SURVEY LOKASI!!!!"

    mc "Wah mana udah H-1 lagi, berarti hari ini kesempatan terakhirku buat ngecek lokasi SNBT nya biar ngga kebingungan
    waktu SNBT nanti"

    mc "Hmm... tapi rasanya karena udah H-1 aku harus lebih mengingat dan mempelajari materi yang belum kupahami"

    mc "Tapi anggap aja buat refreshing juga sambil eksplorasi gedung jurusannya, dengan gitu pasti aku akan
    lebih semangat untuk belajar"

    menu:

        "Apakah aku harus survey lokasi SNBT?"

        "Gasss":

            $ eksplor = 1

        "Malasss":

            show unknown

            mc "UWAHHHHH!!!!!!!!!"

            mc "S-S-SsIAPA KAMU???"

            unk "Itu tidak penting. Yang lebih penting adalah kamu harus mengeksplorasi lokasi SNBT mu."

            mc "T-Tapi aku harus mempelajari hal yang belum aku pahami"

            unk "Kutanya lagi, apakah kau tetap tidak ingin eksplorasi atau kau mengubah pikiranmu?"

            menu:
                "Kutanya lagi apakah kau tetap tidak ingin eksplorasi atau kau mengubah pikiranmu?"
                "Aku mengubah pikiranku":
                    
                    $ eksplor = 1

                "Malassssss":
                    
                    unk "Uhhhh..... apakah kamu benar benar tidak ingin eksplorasi?"

                    menu:
                        "Uhhhh..... apakah kamu benar benar tidak ingin eksplorasi?"
                        "Aku mau eksplorasi":
                            
                            $ eksplor = 1

                        "Aku mau eksplorasi":
                            
                            $ eksplor = 1

                        "Malassss":

                            unk "Tolong hargai usaha developer :("

                            menu:
                                "Tolong hargai usaha developer :("
                                "Aku mau menghargai usaha developer":
                                    
                                    $ eksplor = 1

                                "Aku mau menghargai usaha developer":
                                    
                                    $ eksplor = 1

                                "Aku mau menghargai usaha developer":
                                    
                                    $ eksplor = 1

                                "Malassssss":
                                    
                                    unk "Tidaaaaaaakkkkkkkkkk"

                                    hide unknown

                                    "Entitas itu menghilang"

                                    mc "Apa itu barusan?"

                                "Aku mau menghargai usaha developer":
                                    
                                    $ eksplor = 1

                                "Aku mau menghargai usaha developer":
                                    
                                    $ eksplor = 1

                                "Aku mau menghargai usaha developer":
                                    
                                    $ eksplor = 1
                                
    if eksplor == 1:

        hide unknown

        mc "Baiklah ini kesempatan terakhirku buat eksplor tempatnya sebelum SNBT atau aku ditolak :("

        mc "Akan kumanfaatkan sebaik-baiknya kesempatan ini"

        jump diBundaranITS

    else:
        #block of code to run

        mc "Malas le"

        jump hariUTBK

    #return

label diBundaranITS:
    "Ini di bundaran"

    return

label hariUTBK:
    "Ini hari utbk"

    return