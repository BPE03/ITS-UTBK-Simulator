# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[McName]")
define unk = Character("???")
define bpk = Character("Bapak Bapak TU")
define bpka = Character("Bapak Bapak Aula")
define mmh = Character("Mas Mas hengker")
define nbun = Character("Cynthia")
define nr101 = Character("Elisa")
define nr106 = Character("Andi")
define nr109 = Character("Diana")
define nlp2 = Character("Farah")
define nkantin = Character("Bagas")
define nmasjid = Character("Gilang")
define audio.c1 = "<loop 21.44>audio/Sun_Rays.wav"
define satpam = Character("Satpam")

default correctAnswer = 0
default eksplor = 0
default inspectedBundaran = 0
default inspectedGedung1 = 0
default inspectedGedung2 = 0
default inspectedLp2 = 0
default ngobrolBundaran = 0
default ngobrolKantin = 0
default ngobrolMasjid = 0
default ngobrolLp2 = 0
default ngobrol_r101 = 0
default ngobrol_r106 = 0
default ngobrol_r109 = 0
default visited_bundaran = 0
default visited_kantin_via_r109 = 0
default visited_parkiran_via_r101 = 0
default places_discovered = {
    "depanTC": False,
    "gedung1": False,
    "gedung2": False,
    "kantin": False,
    "r101": False,
    "r106": False,
    "r109": False,
    "lt2": False,
    "lt3": False,
    "lp2": False,
    "laboratorium_giga": False,
    "masjid": False,
    "parkiran": False,
    "aula": False,
    "tu": False,
    "lt2_closed": False,
}
init python:
    def discovered_all_places():
        return all(places_discovered.values())

# The game starts here.

label start:

    stop music

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show unknown

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

    unk "Oh ya, game ini dibuat oleh:"

    unk "5025221169 - Bimantara Putra Ernandra\n5025221203 - Muhammad Choirun Ni'Am"

    unk "FSM dari game ini dapat di lihat di gambar berikut"

    unk "...."

    unk "Oh tidak aku tidak punya miro premium :("

    show fsm

    unk "Kamu bisa menekan tombol 'H' untuk menyembunyikan kotak dialog ini.
    jika kamu ingin melihat lebih jelas dapat diakses melalui link ini
    https://miro.com/app/board/uXjVI92-RAM=/?share_link_id=344571530145"

    unk "Melanjutkan dialog ini akan menghilangkan gambar FSM"

    hide fsm

    unk "Ngomong-ngomong..."

    unk "Jika kamu adalah orang yang ingin masuk ke ITS dengan jalur SNBT..."

    unk "Ingatlah kunci agar lulus SNBT itu adalah......."

    hide unknown

    jump prologue

    # This ends the game.
    # return

label prologue:

    mc "Uwahhhhh!!!!!"

    mc "huft... huft...."

    play music c1

    scene kamar
    with fade

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

    mc "Baiklah aku fix akan daftar ke Informatika ITS sebagai pilihan 1"

    mc "Kemudian... lokasi SNBT di ITS juga lah biar peluang sukses makin gede"

    "Padahal itu mitos saja agar peserta yang ingin masuk ke kampusnya jadi lebih semangat."

    "Setelah mendaftarkan diri ternyata aku ditempatkan untuk mengerjakan SNBT di LP2 gedung Informatika"

    mc "Woaah tes nya di gedung Informatika juga ternyata cuy"

    mc "Harus survey lokasi sih ini biar makin positif untuk bisa lolos."

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
            $ renpy.music.set_volume(0.0, delay=1, channel='music')

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

            $ renpy.music.set_volume(1.0, delay=1, channel='music')
                                
    if eksplor == 1:

        hide unknown

        mc "Baiklah ini kesempatan terakhirku buat eksplor tempatnya sebelum SNBT atau aku ditolak :("

        mc "Akan kumanfaatkan sebaik-baiknya kesempatan ini"

        "Aku pun bergegas memesan ojek online untuk segera pergi ke ITS"

        "Untuk tujuan pertamaku, aku ingin mencoba lihat bundaran ITS yang terkenal dengan air mancurnya itu."

        jump diBundaranITS

    else:
        #block of code to run

        mc "Ya, lebih baik mempelajari materi yang aku masih belum sepenuhnya paham"

        mc "Karena waktu belajar ku sudah tinggal hari ini saja."

        "Aku pun memutuskan untuk belajar sepenuhnya di hari ini"

        jump hariUTBK

    #return

label diBundaranITS:

    scene bundaran1
    with fade

    if visited_bundaran == 0:

        $ visited_bundaran = 1

        $ renpy.pause(2.0, hard=True)

        "Sesampainya di bundaran ITS, aku tidak lupa untuk memberi tip ke driver yang barusan mengantarku"

        "Anggap saja ini merupakan satu dari banyak \"jimat\" yang aku beli untuk meningkatkan peluang lolos ku."

        mc "Terima kasih pak!"

        "Setelah driver itu pergi, aku mulai melihat-lihat sekelilingku"

        mc "Hmm jadi ini bundaran ITS."

        "Kemudian dari jauh, nampak ada cewek yang lagi foto-foto gedung-gedung ITS dari sini"

        "Kira-kira apakah dia juga sedang survey lokasi atau hanya sekedar melihat saja?"

    menu:
        "Apa yang harus aku lakukan di sini?"
        "Ajak Ngobrol":
            jump ngobrol_di_bundaran
        "Inspek":
            jump inspekBundaran
        "Pergi Ke Teknik Informatika":
            mc "Jika aku pergi ke Informatika, mungkin aku tidak akan bisa kembali lagi ke sini"

            menu:
                "Yakin pergi ke gedung informatika sekarang?"
                "Ya":
                    mc "Baiklah aku akan ke gedung Informatika sekarang"

                    mc "Maksudku... lebih cepat lebih baik kan?"

                    "Aku mencoba melihat lokasi gedung Informatika melalui peta di ponselku"

                    "Ternyata jauh juga."

                    "Akhirnya aku memutuskan untuk pesan ojek online lagi"

                    if ngobrolBundaran > 0:
                        "Akupun tidak lupa untuk pamit ke Cynthia"

                        mc "Eh Cyn aku pergi duluan yak, lokasi SNBT ku di Teknik Informatika soalnya"

                        show cynthia ketawa

                        nbun "Okeeyy hati-hati ya!"

                        hide cynthia netral

                    jump diDepanTC

                "Nanti dulu":
                    mc "Hmmm... nanti dulu deh, masih ada yang pengen kulihat di sini"

                    jump diBundaranITS

    return

label inspekBundaran:
    if inspectedBundaran == 0:
        $ inspectedBundaran += 1

        "Aku melihat sekelilingku"

        "Yang pertama kali menarik perhatianku adalah tulisan Institut Teknologi Sepuluh Nopember yang 
        ada di pinggir sepanjang jalan bundaran"

        mc "Seumur hidupku lewat jalan ga pernah ada tulisan almamater segede ini"

        mc "tempatnya di bundaran juga, otomatis pasti banyak orang yang lihat"

        mc "kalo aku bisa lolos ke kampus ini, jelas akan aku pamerkan almamaterku"

    elif inspectedBundaran == 1:
        $ inspectedBundaran += 1

        "Aku melihat-lihat sekelilingku lagi"

        "Aku melihati kendaraan-kendaraan yang melewati bundaran"

        "Kemudian pandanganku terpaling ke pilar pilar yang ada di awal dan di akhir bundaran"

        "Di atasnya ada tulisan Institut Teknologi Sepuluh Nopember"

        mc "Saat browsing kampus tadi aku bingung kenapa banyak banget orang-orang yang pada pengen kuliah di sini"

        mc "Sekarang aku tau"

        mc "Kampus ini mewah banget buat level kampus negeri"

    elif inspectedBundaran == 2:
        $ inspectedBundaran += 1

        "Aku melihat-lihat sekelilingku"

        "Di tengah bundaran seperti ada tanda dilarang menginjak rumput"

        "Hmmm"

        mc "Oh iya tujuanku ke sini kan pengen liat air mancurnya"

        mc "Hmmm aku lupa browsing lagi kalo pagi nyala apa ga"

        "Sesaat setelah aku mengatakan itu"

        "Tiba-tiba..."

        scene air_mancur_bundaran
        with fade

        $ renpy.pause(2.0, hard=True)

        mc "Woaah..."

        "Air mancur yang kukira tidak menyala di pagi hari..."

        "Sekarang menyembur di mata ku"

        mc "Wohh gilak keren banget sih ini"

        mc "Aku foto ah"

        "Aku pun bergegas memfotonya sebelum air mancurnya berhenti lagi"

        mc "Mantap cuy fotonya, langsung jadiin story sih ini"

        "Tidak berselang lama, air mancur itu berhenti menyemburkan airnya"

        mc "Oh airnya udah ngga mancur lagi"

        mc "Walaupun bentar tapi liatnya udah puas"

        mc "Kalo bisa sih aku bakal ke sini lagi waktu malam, pasti lebih keren lagi waktu ada lampunya"

    else:
        "Aku melihat-lihat sekelilingku...."

        "Kurasa aku sudah melihat semua yang ada di sini"

    jump diBundaranITS

label ngobrol_di_bundaran:

    if ngobrolBundaran == 0:
        $ ngobrolBundaran += 1

        "Aku memutuskan untuk mengajak ngobrol cewek itu"

        "Siapa tau kalau dia ingin kuliah di ITS juga"

        mc "Kampusnya keren ya mbak?"

        show cynthia netral

        unk "...."

        "Ah ga dijawab lagi, apa aku salah mulainya ya?"

        mc "halo mbak?"

        hide cynthia netral
        show cynthia kaget

        unk "Eh iya mas, ada apa ya?"

        mc "Oh ngga tadi aku liat mbaknya lagi foto-foto kampusnya tadi, pengen kuliah di sini kah mbak?"

        hide cynthia kaget
        show cynthia netral

        unk "Iya mas, sekalian survey lokasi SNBT juga"

        mc "Loh sama nih, aku juga pengen kuliah di ITS juga, SNBT nya juga ngerjain di ITS. ngomong ngomong
        mau masuk jurusan mana mbak?"

        unk "Aku pengennya masuk Teknologi Kedokteran sih pilihan pertamanya, ya tapi kalo ngga dapet
        pilihan kedua ku di Teknik Kimia. Kalo masnya ambil jurusan apa?"

        mc "Aku sih ngambil Teknik Informatika di pilihan pertamanya, pilihan keduanya jujur ngga tau haha,
        tapi yang mirip mirip sih di Sistem Informasi jadi itu pilihan kedua ku."

        hide cynthia netral
        show cynthia kaget

        unk "Wihh kerenn..... yakin lolos mas? itu keduanya passing-gradenya tinggi banget loh"

        hide cynthia kaget
        show cynthia netral

        mc "Harus yakin dong, kalo ga yakin gimana bisa lolos kalo mentalnya down duluan? dari SD sampe SMA
        aku selalu percaya diri meskipun masih ada materi yang belum aku bener bener pahami."

        mc "Kalo udah yakin, mentalnya tenang, pasti waktu ngerjain juga bakal dateng dengan sendiri ilmunya"

        "Aku ngomong begitu dengan pedenya"

        "Padahal mah aku selalu beruntung aja bisa dapet nilai sesuai ekspektasi"

        "Emang aku bisa lolos di jurusan dengan peminat terbanyak hanya ngandelin beruntung doang?"

        hide cynthia netral
        show cynthia ketawa

        unk "Wih bener banget sih itu, semoga lolos ya mas"

        mc "Amiin kamu juga ya. BTW boleh kenalan ga?"

        hide cynthia ketawa
        show cynthia netral

        nbun "Boleh mas, kenalin aku Cynthia"

        mc "Cynthia... kenalin aku [McName]. Salam kenal ya"

        nbun "Salam kenal juga"

        hide cynthia netral

    elif ngobrolBundaran == 1:

        $ ngobrolBundaran += 1

        mc "BTW Cynthia, persiapan SNBT mu gimana aman ga?"

        show cynthia netral

        nbun "Alhamdulillah liat hasil Try-Out ku yang selalu di atas passing grade, aku optimis sih
        bisa lolos. Kalo kamu gimana?"

        mc "Yaa.... aku udah nyoba pelajarin hasil try out ku yang hasilnya kayak uang koin itu....
        ya semoga beruntung aja sih, biasanya kurang bisa mikir cepat aku walaupun udah paham soalnya"

        nbun "uang koin berapa mas? 100? 200?"

        hide cynthia netral
        show cynthia ketawa

        "Buset dia ketawa lagi."

        "Jadi malu aku, hasil TO nya dia dah aman banget, lah aku hasil pas pasan gini malah sok ngasih
        kata kata motivasi"

        mc "Kalo nilaiku segitu udah aku buang jauh jauh sih koin sama harapanku"

        hide cynthia ketawa
        show cynthia netral

        nbun "ahaha bercanda aja mas, omong-omong soal mana mas yang kesulitan? barangkali bisa aku bantu"

        mc "hmm di semua subtes pasti ada soal yang aku mikirnya lama, nilai subtesmu yang paling bagus
        di mana Cyn?"

        nbun "kalo aku paling bagus di Pengetahuan Kuantitatif ya, tapi terkadang aku juga ngga sepenuhnya
        semua kukerjain. Kalo waktunya mepet banget aku langsung nembak B."

        "Pengetahuan Kuantitatif....."

        "Ya, nih anak jenius"

        mc "buset pengetahuan kuantitatif tertinggi? keren sih kamu Cyn"

        nbun "Hehe aku emang suka banget sama matematika dari SMP, semenjak itu aku selalu coba-coba soal yang
        menurutku menantang, dengan gitu lama kelamaan kecepatan ngitungku jadi cepet juga"

        mc "Hmmmm i see... makasih buat tipsnya yak"

        nbun "Sama-samaa~"

        hide cynthia netral

    elif ngobrolBundaran == 2:
        $ ngobrolBundaran += 1

        mc "Btw kalo misal kamu ga lolos SNBT gimana Cyn?"

        show cynthia kaget

        nbun "Loh kok tanya gitu, katanya tadi harus yakin?"

        mc "Bener yakin itu penting, tapi tetep aja ngga menutupi worst casenya juga kan, karena
        aku juga bingung kalo ngga lolos nanti harus gimana lagi"

        mc "Mandiri? darimana duitnya, gap year? ya mungkin pilihan terbaikku buat belajar lebih banyak lagi"

        hide cynthia kaget
        show cynthia netral

        nbun "mmmm...."

        nbun "Belum kepikiran sih mas, karena daripada mikirin gimana kalo ga lolos, mending mikirin gimana
        supaya lolos"

        nbun "Kan masnya sendiri yang bilang tadi harus yakin, kalo yakin lolos ngapain mikirin worst case?
        mikirin itu yang ada nambah beban pikiran juga mas"

        "Seketika aku merenung sedikit"

        "Iya juga ya"

        "Ngapain aku mikirin worst case?"

        "Kalo aku emang yakin lolos"

        "Seharusnya aku ngga perlu mikirin itu"

        mc "Iya juga ya haha, makasih motivasinya yak"

        hide cynthia netral
        show cynthia ketawa

        nbun "Okeyy~"

        hide cynthia ketawa

    elif ngobrolBundaran == 3:
        $ ngobrolBundaran += 1

        mc "Btw kalo udah lolos ITS nanti rencananya mau ngapain aja?"

        show cynthia netral

        nbun "Belum tau sih mas, yang pasti aku pengen nyoba ikut riset kalo ada, 
        atau pengen nyoba teoriku yang lagi aku kembangin yaitu bikin alat untuk ngobatin kanker"

        "...."

        "Kalo aku bilang dia jenius kayaknya masih kurang deh"

        mc "Kamu udah bikin penelitian sendiri?"

        nbun "Iya, tapi karena ngga ada fasilitasnya jadi aku ngga bisa nyoba, makanya aku pengen banget
        buat masuk ke jurusan ini"

        "Ya aku hanya berharap kamu tidak ada di pesawat aja"

        mc "Aku ngga tau sih mau ngomong apa lagi"

        mc "Rasanya apapun rencana yang mau aku ceritain kaya ngga ada apa apanya haha"

        nbun "Gapapa mas cerita aja, ngga adil dong kan aku udah cerita masa kamu ngga"

        mc "Waduh oke deh, jadi rencanaku setelah masuk ke Informatika itu ya pengen nyoba bikin game gitu"

        hide cynthia netral
        show cynthia kaget

        nbun "Oh masnya suka main game kah?"

        hide cynthia kaget
        show cynthia netral

        mc "Iya karena aku suka main game, aku jadi mikir kok bisa ya orang orang bikin game kayak gini. 
        Apalagi ada 1 game yang bener bener bikin perspektif ku ke game itu berbeda banget"

        mc "Dulu waktu aku kecil aku selalu dimarahin orang tuaku dengan alasan NGEGAME TEROSS, kuakui
        mungkin mereka ada benarnya karena dulu aku bermain game karena hanya sekedar bersenang senang aja"

        mc "Dan dulu aku sering sekali bermain game yang punya elemen kompetitif, waktuku jadi terbuang sia-sia
        hanya untuk mencari validasi dengan pamer rank yang tinggi, sudah tidak menyenangkan, waktuku juga hilang
        begitu saja."

        mc "Tapi sekarang? game yang aku mainkan selalu tipe game yang Single Player dengan story dan karakter
        yang bagus. Game game tersebut lebih menyenangkan dan edukatif daripada game yang tujuannya untuk naik
        rank"

        mc "Dari situlah aku benar benar paham apa yang membuat orang orang selalu menyalahkan game ketika anaknya
        malas belajar"

        mc "Mereka memainkan game yang salah."

        mc "Game yang seharusnya menyenangkan, mereka malah bekerja di game itu"

        mc "Aku tidak tahu kenapa game seperti itu bisa lebih populer dari game yang santai dan menyenangkan"

        mc "Maka dari itulah aku ingin membuat game yang bisa diakses untuk semua umur, menyenangkan,
        dan pastinya mengedukasi mereka."

        hide cynthia netral
        show cynthia ketawa

        nbun "Jujur aku ngga tau apa apa tentang game mas, tapi apapun rencana masnya semoga bisa kecapai ya"

        mc "Kamu juga Cyn."

        hide cynthia ketawa

    else:
        mc "Aku tidak tahu topik apalagi yang ingin kubicarakan"

    jump diBundaranITS

label diDepanTC:
    scene depantc
    with fade
    if places_discovered["depanTC"] == False:
        $ places_discovered["depanTC"] = True
        "Sesampainya di depan gerbang Informatika, aku tidak lupa untuk memberi driverku tip"

        "Hmmm...."

        "Jadi ini gedung Informatika"

        scene tc_depan

        "Di depan gedung ini ada tulisan Teknik Informatika"

        "Benar-benar eksotis, aku merasa bisa jadi orang paling hebat jika lolos ke jurusan ini di kampus ini"

        scene depantc

        "Baiklah mungkin selanjutnya aku mau eksplorasi semua yang ada di gedung ini"

        "Maksudku itu dapat membuatku semakin yakin untuk lolos kan?"

        "Jika aku merasa sudah mengunjungi semua tempat aku bisa pulang dengan memesan ojek online lagi di sini."

    menu:
        "Apa yang harus aku lakukan di sini?"
        "Ke Kiri" if not places_discovered["kantin"]:
            "Aku mencoba pergi ke sebelah kiri dari gedung..."
            jump diKantin

        "Ke Kantin" if places_discovered["kantin"]:
            "Aku pergi ke kantin..."
            jump diKantin

        "Masuk":
            "Aku masuk ke gedung Informatika...."
            jump diGedung1

        "Ke Kanan" if not places_discovered["parkiran"]:
            "Aku mencoba pergi ke sebelah kanan dari gedung..."
            jump diParkiran

        "Ke Parkiran" if places_discovered["parkiran"]:
            "Aku pergi ke parkiran..."
            jump diParkiran

        "Balik ke bundaran":
            jump malasBalik

        "Pulang":
            if discovered_all_places():
                "Aku sudah melihat semuanya di sini"

                "Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                jump hariUTBK

            else:
                "Aku rasa masih ada tempat yang belum aku kunjungi"

                "Sebaiknya aku eksplor seluruh tempat ini"

                jump diDepanTC

    return

label malasBalik:
    "Balik ke bundaran?"

    "Yang bener aja panas panas gini aku balik ke tempat terbuka gitu?"

    "Malas ah"

    jump diDepanTC

label diKantin:
    scene kantin
    with fade
    if not places_discovered["kantin"]:
        $ places_discovered["kantin"] = True

        "Ternyata ini adalah kantin dari Informatika"

        mc "Oh kantinnya di sebelah sini ternyata"

        mc "Ada menu apa aja ya?"

        "Aku melihat menu di kantin"

        mc "Hmm lumayan variatif juga ya menunya"

        "Aku terlalu fokus dengan melihat menu sampai-sampai aku tidak melihat ada orang di belakangku"

        unk "Permisi mas"

        mc "Oh iya silakan"

        "Hmm seharusnya kalau mendekati SNBT mahasiswa di sini tidak ada pembelajaran kan? karena ruang kelasnya
        dijadikan tempat SNBT."

        "Apakah dia juga lagi survey lokasi?"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
                
    menu:
        "Apa yang harus aku lakukan di sini?"
        "Ajak Ngobrol":
            jump ngobrol_di_kantin

        "Inspek":
            jump inspekKantin

        "Kembali ke depan gedung Informatika":
            "Aku kembali ke depan gedung Informatika..."
            jump diDepanTC

        "Ke belakang gedung Informatika" if visited_kantin_via_r109 == 1:
            "Aku kembali ke gedung Informatika lewat belakang..."
            jump r109
    return

label ngobrol_di_kantin:
    if ngobrolKantin == 0:
        $ ngobrolKantin += 1

        "Aku mencoba ngajak ngobrol anak itu"

        mc "Permisi mas, masnya lagi survey lokasi SNBT kah"

        show bagas netral

        unk "Oh iya mas"

        mc "Ohh sama nih mas lokasi SNBT ku juga di sini, kalo boleh tau masnya ambil jurusan mana mas?"

        unk "lek bisa lolos sih aku ambil informatika ITS sini sih mas"

        unk "Tapi nilai TO ku sek belum nyentuh passing grade blas e"

        mc "Oalah gapapa mas semangat aja, dari pengalaman kakak kelasku yang lolos SNBT juga gitu"

        mc "Nilainya waktu TO 500an terus"

        mc "Tapi waktu di SNBT ternyata bisa tembus 700"

        mc "Padahal ya mereka ngerjainnya sama aja kayak waktu ngerjain TO"

        hide bagas netral
        show bagas ketawa

        unk "Owalah iyo ta mas? wes dadi semangat ngene seh aku, makasih yo mas"

        mc "Okee, btw boleh kenalan ga? aku [McName]"

        nkantin "Bolehh, aku Bagas mas"

        mc "Oke salam kenal ya"

        nkantin "Salam kenal juga mas"

        hide bagas netral
    elif ngobrolKantin == 1:
        $ ngobrolKantin += 1

        mc "Btw kalo bisa lolos mau ngapain aja mas"

        show bagas netral

        nkantin "Kalo bisa lolos seh aku pengen bikin game ya, game tipe tipe RPG gitu karena suka banget
        aku sama game game kek gitu"

        mc "Loh beneran mas? sama nih aku juga pengen bikin game RPG"

        hide bagas netral
        show bagas kaget

        nkantin "Waduh...."

        nkantin "Bikin sekarang ae mas wes daripada nunggu lolos malah ga bikin bikin"

        hide bagas kaget
        show bagas netral

        mc "Ohh aku masih belum tau caranya haha, makanya nunggu lolos dulu"

        hide bagas netral
        show bagas ketawa

        nkantin "Oalah gitu ta mas, yowes semangat lah ya"

        mc "Sama-sama"

        hide bagas ketawa
    elif ngobrolKantin == 2:
        $ ngobrolKantin += 1

        mc "Oiya nilai tertinggimu di subtest apa, ada tips ga?"

        show bagas netral

        nkantin "Aku tertinggi di PPU seh mas, karena aku kan yo sering main game yang tipe problem solving
        gitu jadine aku cepet buat ngerjain tipe tipe soal di PPU"

        nkantin "Ya banyakin latihan soal aja seh mas ntar juga polane pasti ada seng sama"

        nkantin "Kalopun waktune mepet yo aku selalu nembak E dan bisa dapet nilai sing bagus"

        mc "Ohh jadi kunci nya banyakin latihan soal aja ya mas?"

        nkantin "Betul"

        mc "Wokeehh makasih mas"

        hide bagas netral
        show bagas ketawa

        nkantin "Yoii"

        hide bagas ketawa
    else:
        "Aku tidak tahu topik apalagi yang ingin kubicarakan"

    jump diKantin

label inspekKantin:
    "Tidak banyak yang bisa dilihat di sini"

    "Kantin ini layaknya kantin pada umumnya dengan beberapa set meja dan kursi"

    "Ada tempat yang memiliki 2 kursi untuk 1 meja, adapula 1 meja yang memiliki 4 kursi"

    "Menu yang dijual juga cukup beragam, ada Nasi Campur, Nasi Goreng, Nasi Ayam, Mi Ayam
    dan masih banyak lagi"

    "Ada tempat untuk membeli minuman juga yang disimpan di kulkas seperti di minimarket"

    "Jika menghadap sebelah barat aku bisa menikmati hidangan dengan pemandangan sawah yang menyejukkan"

    mc "Cukup oke sih menurutku"

    jump diKantin

label diGedung1:
    scene gedung1
    with fade
    if not places_discovered["gedung1"]:
        $ places_discovered["gedung1"] = True

        "Aku akhirnya menempatkan kakiku di gedung ini"

        "Aku disambut dengan baliho ucapan selamat atas prestasi mahasiswa jurusan ini"

        mc "Gila banyak banget!"

        "Seharusnya aku ngga kaget melihat kemampuan anak yang bisa ngalahin 2.000 peserta SNBT yang lain."

        "Tapi tetep aja ini pertama kali aku ngelihat baliho penghargaan sebesar ini"

        mc "Kalau namaku ada di situ sudah pasti terkenal sih"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    menu:
        "Apa yang harus aku lakukan di sini?"

        "Inspek":
            jump inspekGedung1
        "Maju Kiri" if not places_discovered["r109"]:
            "Aku maju ke lorong kiri..."
            jump r109

        "Ke Lorong Ruang 109-113" if places_discovered["r109"]:
            "Aku maju ke lorong kiri..."
            jump r109

        "Maju Kanan" if not places_discovered["r106"]:
            "Aku maju ke lorong kanan..."
            jump r106

        "Ke Lorong Ruang 106-108" if places_discovered["r106"]:
            "Aku maju ke lorong kanan..."
            jump r106

        "Naik Tangga":
            scene tangga_naik
            "Aku menaiki Tangga..."

            jump lt2

        "Keluar":
            "Aku keluar dari sini..."
            jump diDepanTC
    return

label inspekGedung1:
    if inspectedGedung1 == 0:
        $ inspectedGedung1 += 1
        "Aku melihat-lihat di sekelilingku..."

        "Ya pandanganku masih tidak bisa berpaling dari baliho tersebut"

        "Mari kita lihat..."

        "Tim Barunastra ITS mendapatkan gelar juara dunia pada International Roboboat Competition 2025"

        "...."

        "Dunia??"

        "Juara dunia???"

        "Lebih unggul dari kampus luar negeri seperti MIT?"

        "Ternyata aku tidak sedang menginjakkan kaki ke kampus negeri"

        "Aku menginjakkan kakiku ke kampus luar negeri dalam negeri"

        "Maksudku tidak banyak di negara ini yang dapat menyaingi negara luar"
    elif inspectedGedung1 == 1:
        $ inspectedGedung1 += 1

        "Aku melihat sekelilingku lagi"

        scene depan_toilet

        mc "Oh toiletnya di sebelah sini ternyata"

        "Aku mencoba masuk ke toiletnya..."

        scene wastafel

        "Yap standar"

        scene toilet

        "Kemudian terlihat model WC duduk dari toilet yang terbuka"

        "Jujur aku lebih suka model WC jongkok"

        "Rasanya bisa keluar lebih banyak dan lebih puas daripada WC duduk"

        "Hmm...?"

        "Satu pintu toillet yang tertutup itu tiba-tiba terbuka"

        "Orang itu langsung datang ke arahku"

        show bapak bapak tu

        bpk "Mas ini toilet khusus dosen, toilet khusus mahasiswa di sebelah sana"

        mc "Oh iya maaf pak saya nggak tau"

        "Aku bergegas keluar dari toilet"

        scene gedung1
        with fade

        "Hufft..."

        "Untung saja tidak terjadi apa-apa"

        "Ya mungkin aku harus lebih berhati-hati lagi sebelum memasuki suatu ruangan."

    elif inspectedGedung1 > 1:
        "Nampaknya sudah tidak ada hal baru yang bisa kulihat"
    jump diGedung1

label r109:
    scene r109
    with fade
    if not places_discovered["r109"]:
        $ places_discovered["r109"] = True

        "Nampaknya seperti lorong biasa yang berisikan kelas-kelas"

        "Aku juga melihat ada anak yang sedang duduk di salah satu kursi di sini"

        "Apakah dia salah satu mahasiswa atau anak yang lagi survey juga?"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"

    menu:
        "Apa yang harus aku lakukan di sini?"
        "Ajak Ngobrol":
            jump ngobrol_di_r109

        "Inspek":
            jump inspekR109

        "Maju terus" if visited_kantin_via_r109 == 0:
            $ visited_kantin_via_r109 = 1

            "Aku mencoba terus maju ke belakang gedung...."

            scene kantin

            "Ternyata jalan di belakang gedung ini bisa sebagai jalan pintas untuk ke kantin"

            mc "Oww ada jalan pintas juga rupanya"

            mc "Kalo gini bisa cepet ke kantin dong dari kelas
            daripada aku harus mutar jauh cuma untuk ke kantin"

            mc "Bisa-bisa meninggal duluan aku"

            jump diKantin

        "Ke Kantin" if visited_kantin_via_r109 == 1:
            "Aku pergi ke kantin..."
            jump diKantin

        "Ke Tempat Masuk Gedung Informatika":
            "Aku berjalan ke arah timur..."
            jump diGedung1        

label inspekR109:
    scene kiri_lt1
    "Hanya lorong biasa yang berisikan ruang kelas dan ada lab untuk mahasiswa pascasarjana juga"

    "Ada kelas 109, 110, 111, 112, dan 113 di sini"

    scene r109
    "Di bagian utara dari sini ada beberapa tempat duduk serta meja untuk belajar"

    scene plasa
    "Lebih jauh ada semacam tempat belajar outdoor yang cukup luas"

    scene lapangan
    "Dan lebih keluar lagi ada lapangan untuk melakukan berbagai aktivitas olahraga"

    scene panggung
    "Kemudian di belakang lapangan itu ada panggung yang kemungkinan digunakan untuk acara-acara mahasiswa"

    scene musholla
    "Aku juga dapat melihat musholla di bagian barat laut yang dekat dengan bagian belakang dari gedung ini"

    jump r109

# Unfinished
label ngobrol_di_r109:
    if ngobrol_r109 == 0:
        $ ngobrol_r109 += 1
        "Aku mencoba mengajak ngobrol anak itu"

        mc "Halo mbak, mbaknya survey lokasi SNBT juga kah?"

        unk "Iya"

        mc "Oh sama nih, mau kuliah di ITS juga kah mbak atau tes di sini karena deket aja?"

        unk "Karena deket aja sih"

        mc "Oh okee, btw boleh kenalan ga? aku [McName]"

        nr109 "Oh aku Diana"

        mc "Salam kenal Diana"

        nr109 "Ya"
    elif ngobrol_r109 == 1:
        $ ngobrol_r109 += 1
        mc "Btw persiapan SNBT mu gimana aman kah?"

        nr109 "aku full B ajalah, PU bisa tembus 700"

        mc "Wow serius? kalo iya mantap sih"

        nr109 "Ya"

        "...."

        "Nampaknya dia sedang tidak ingin bicara"

        "Sebaiknya tidak aku ganggu lagi"
    else:
        "Aku tidak punya topik untuk dibicarakan"

    jump r109

label r106:
    scene r106
    with fade
    if not places_discovered["r106"]:
        $ places_discovered["r106"] = True

        "Nampaknya seperti lorong biasa yang berisikan kelas-kelas"

        "Aku juga melihat ada anak yang sedang duduk di salah satu kursi di sini"

        "Apakah dia salah satu mahasiswa atau anak yang lagi survey juga?"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"

    menu:
        "Apa yang harus aku lakukan di sini?"
        "Ajak Ngobrol":
            jump ngobrol_di_r106
        "Inspek":
            jump inspekR106
        "Maju" if not places_discovered["gedung2"]:
            "Aku maju terus ke arah utara..."
            jump diGedung2
        "Ke Gedung Informatika bagian Utara" if places_discovered["gedung2"]:
            "Aku maju terus ke arah utara..."
            jump diGedung2
        "Ke Gedung Informatika bagian Selatan":
            "Aku maju terus ke arah selatan..."
            jump diGedung1

label ngobrol_di_r106:
    if ngobrol_r106 == 0:
        $ ngobrol_r106 += 1

        "Aku mencoba menghampiri anak itu"

        mc "Permis mas, masnya survey lokasi SNBT juga kah?"

        show andi ketawa

        unk "Yoww whatsapp my N****? yes aku habis survey lokasi buat SNBT ini"

        mc "Loh mas ini game edukasi mas jangan ngomong aneh aneh"

        hide andi ketawa
        show andi kaget

        unk "Hah maksud e?"

        mc "Uhh lupakan aja aku ngomong apa tadi, berarti masnya pengen kuliah di ITS?"

        hide andi kaget
        show andi netral

        unk "Yoii"

        mc "Pengen kuliah di jurusan mana mas?"

        unk "Informatika dongg gamer masa ngga ngoding, ya kalo ngga keterima sih aku sek berharap
        lolos Sistem Informasi lah"

        mc "Woww lumayan juga ya mas kedua jurusannya, kebetulan aku juga pengen masuk informatika nih"

        hide andi netral
        show andi kaget

        unk "Seriusan???"

        hide andi kaget
        show andi ketawa

        unk "My boyy"

        unk "Good luck lah yak"

        mc "Okee sama-sama bang, btw boleh kenalan ga? kenalin aku [McName]"

        hide andi ketawa
        show andi netral

        nr106 "Oww [McName] kenalin aku Andi"

        mc "Okee salam kenal Andi"

        nr106 "Salam kenal juga"
    elif ngobrol_r106 == 1:
        $ ngobrol_r106 += 1

        mc "Btw persiapan SNBT gimana aman kah?"

        show andi netral

        nr106 "Hadeuhh ini yang bikin deg-degan"

        nr106 "Nilai TO ku ngga naik naik men, stuck di 600 ke bawah terus"

        nr106 "Padahal udah sering banget ikutan TO gini"

        mc "Oww... sama sih nilaiku juga masih stuck di uang koin"

        hide andi netral
        show andi ketawa

        nr106 "AHAHAHAHA"

        hide andi ketawa
        show andi netral

        nr106 "Gile emang susah banget soal-soalnya yak, udah gitu waktunya dikit lagi"

        nr106 "Aku jadi selalu bergantung di nilai bahasa inggrisku terus"

        mc "Ohh berarti nilai tertinggimu di bahasa inggris yak? boleh kasih tips ga biar
        aku bisa improve di bahasa inggris ku?"

        nr106 "Banyak-banyakin baca aje sih bang, aku sering baca majalah majalah bahasa inggris gitu"

        nr106 "Lama kelamaan aku jadi tau nih caranya nentuin ide utama, makna paragraf, makna tersirat,
        ya pokoknya yang ada di soalnya lah"

        nr106 "Tapi kalo ngga sempet ngerjain aku nembak D sih bang, meskipun gitu nilaiku tetep mantap
        bahasa inggrisnya"

        mc "Ohh banyakin baca ya bang, okee makasih tipsnya yak"

        nr106 "Yoii"

        hide andi netral
    elif ngobrol_r106 == 2:
        $ ngobrol_r106 += 1

        mc "Rencana kalo udah lolos mau ngapain bang?"

        show andi netral

        nr106 "Kalo bisa lolos ya aku fokus jaga nilai IPK ku aja sih biar ntar bisa dapet beasiswa
        sama gampang cari kerjaan aja"

        mc "Ohh fokus belajar aja ya bang jadinya"

        nr106 "Iyes, sama kalo bisa aku bakal ngelanjutin ngeyoutube sih"

        mc "Oh kamu ada channel youtube bang?"

        hide andi netral
        show andi ketawa

        nr106 "Yoii don't forget to like and subscribe to Jaequiin ya gaes ya"

        "Aku mencoba melihat akun youtubenya melalui hp ku..."

        mc "Wow 36k Subscriber? mantap banget sih ini bang"

        hide andi ketawa
        show andi netral

        nr106 "Yoii jangan lupa share ke temen temenmu juga ye bang bantuin adsense ku"

        mc "Amann, berarti kamu juga suka main catur bang? kulihat lihat videonya tentang catur semua"

        nr106 "Yoii kebetulan hoki aje sih bang karena aku bikinnya waktu pandemi. di situ catur lagi
        populer populernya"

        nr106 "Tapi sekarang entah kenapa udah mulai berkurang yang minat"

        mc "Ohh bener banget sih itu bang, ngikutin pasar bisa kebawa arus juga"

        mc "ya mungkin pasarnya catur emang udah mulai redup ya,
        jujur aku ga pernah main catur jadi ga tau"

        nr106 "Yaa... pokoknya share aja bang ke temen temen abang barangkali ada yang minat"

        mc "Okee siap good luck ya!"

        hide andi netral
        show andi ketawa

        nr106 "Yoii"

        hide andi ketawa
    else:
        "Aku sudah tidak punya topik yang ingin kubicarakan"

    jump r106

label inspekR106:
    "Hanya lorong biasa yang berisikan ruang kelas"

    "Di sini ada kelas 106, 107, dan 108."

    "Di bagian barat dari sini ada beberapa tempat duduk serta meja untuk belajar"

    scene plasa
    "Lebih jauh ada semacam tempat belajar outdoor yang cukup luas"

    scene lapangan
    "Dan lebih keluar lagi ada lapangan untuk melakukan berbagai aktivitas olahraga"

    scene panggung
    "Kemudian di belakang lapangan itu ada panggung yang kemungkinan digunakan untuk acara-acara mahasiswa"

    scene musholla
    "Aku juga dapat melihat musholla di bagian barat laut yang dekat dengan bagian belakang dari gedung ini"

    jump r106

label diGedung2:
    scene gedung2
    with fade
    if not places_discovered["gedung2"]:
        $ places_discovered["gedung2"] = True

        "Jika aku keluar dari sini maka aku bisa langsung ke parkiran motor"

        mc "Jika sewaktu waktu aku kuliah di kelas bagian gedung ini"

        mc "Maka aku harus cepat cepat belajar mengendarai motor"

        mc "Daripada harus jalan sejauh ini dari depan"

        mc "Apalagi waktu terlambat, bisa-bisa belajar di luar aku"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    menu:
        "Apa yang harus aku lakukan di sini?"
        "Inspek":
            jump inspekGedung2
        "Naik Tangga":
            jump mau_ke_lt2
        "Maju kiri" if not places_discovered["r106"]:
            "Aku pergi ke arah kiri depan..."
            jump r106
        "Ke lorong Ruang 106-108" if places_discovered["r106"]:
            "Aku pergi ke lorong ruang 106-108..."
            jump r106
        "Maju kanan" if not places_discovered["r101"]:
            "Aku pergi ke arah kanan depan..."
            jump r101
        "Ke lorong Ruang 101-105" if places_discovered["r101"]:
            "Aku pergi ke lorong ruang 101-105..."
            jump r101
        "Keluar":
            jump diParkiran
        
label mau_ke_lt2:
    if not places_discovered["lt2_closed"]:
        $ places_discovered["lt2_closed"] = True

        "Aku mencoba membuka pintu yang menghalangi tangga"

        mc "Oh pintunya dikunci"

        "Jika aku ingin naik ke lantai 2, aku harus mencari tangga yang lain."

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    else:
        "Jika aku ingin naik ke lantai 2, aku harus mencari tangga yang lain."
    jump diGedung2

label inspekGedung2:
    if inspectedGedung2 == 0:
        $ inspectedGedung2 += 1
        "Aku melihat-lihat di sekelilingku..."

        "Di sini ada baliho ucapan selamat ke mahasiswa berprestasi"

        "Mari kita lihat..."

        "ITS berhasil meraih total delapan medali dalam kompetisi Gemastik XVII 2024"

        "...."

        "Wow"

        "Delapan medali? dari berapa lomba yang ada?"

        "Yang kutahu adalah gemastik itu adalah ajang di tingkat Nasional"

        mc "Berapa dari mahasiswa berprestasi yang kuliah di sini?"

        "Aku pasti bisa menjadi seperti mereka"
    elif inspectedGedung2 == 1:
        $ inspectedGedung2 += 1

        "Aku melihat sekelilingku lagi"

        scene depan_toilet

        mc "Oh toiletnya di sebelah sini ternyata"

        "Aku mencoba masuk ke toiletnya..."

        scene wastafel

        "Yap standar"

        scene toilet

        "Kemudian terlihat model WC duduk dari toilet yang terbuka"

        "Jujur aku lebih suka model WC jongkok"

        "Rasanya bisa keluar lebih banyak dan lebih puas daripada WC duduk"

    elif inspectedGedung2 > 1:
        "Nampaknya sudah tidak ada hal baru yang bisa kulihat"

    jump diGedung2

label r101:
    scene r101
    with fade
    if not places_discovered["r101"]:
        $ places_discovered["r101"] = True

        "Nampaknya seperti lorong biasa yang berisikan kelas-kelas"

        "Aku juga melihat ada anak yang sedang duduk di salah satu kursi di sini"

        "Apakah dia salah satu mahasiswa atau anak yang lagi survey juga?"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    menu:
        "Apa yang harus aku lakukan di sini?"
        "Ajak ngobrol":
            jump ngobrol_di_r101
        "Inspek":
            jump inspekR101
        "Ke Musholla":
            "Aku pergi ke musholla...."
            jump masjid
        "Ke gedung bagian utara":
            jump diGedung2
        "Maju Kanan" if visited_parkiran_via_r101 == 0:
            $ visited_parkiran_via_r101 = 1

            "Aku mencoba terus maju..."

            scene parkiran
            with fade

            mc "Oh ternyata bisa ke parkiran juga ya"

            mc "Ya bagus sih biar yang parkirnya di belakang banget ga perlu jauh jauh untuk masuk ke gedungnya"
            jump diParkiran
        "Ke Parkiran" if visited_parkiran_via_r101 == 1:
            jump diParkiran

label inspekR101:
    "Hanya lorong biasa yang berisikan ruang kelas"

    "Di sini ada kelas 105, 104, 103, 102, dan 101."

    "Di bagian selatan dari sini ada beberapa tempat duduk serta meja untuk belajar"

    scene plasa
    "Lebih jauh ada semacam tempat belajar outdoor yang cukup luas"

    scene lapangan
    "Dan lebih keluar lagi ada lapangan untuk melakukan berbagai aktivitas olahraga"

    scene panggung
    "Kemudian di belakang lapangan itu ada panggung yang kemungkinan digunakan untuk acara-acara mahasiswa"

    scene musholla
    "Aku juga dapat melihat musholla di bagian barat yang dekat dengan bagian belakang dari gedung ini"

    jump r101

label ngobrol_di_r101:
    if ngobrol_r101 == 0:
        $ ngobrol_r101 += 1

        "Aku mencoba menghampiri anak itu"

        show elisa netral1

        "...."

        "Dia nampaknya sedang duduk melamun sambil melihati ruangan-ruangan yang ada di lantai atas"

        "Aku akhirnya memberanikan diri untuk membuka topik"

        mc "Permisi mbak, mbaknya survey lokasi SNBT juga kah?"

        hide elisa netral1
        show elisa netral2

        unk "Oh iyaa, aku barusan selesai nih"

        mc "Ohh mbaknya mau kuliah di ITS kah kok lokasi SNBT nya di ITS juga?"

        unk "Iyaa kebetulan rumahku deket sini jadi sekalian tes di sini jugaa"

        mc "Ohh i see... kalo boleh tahu mau ambil jurusan mana mbak?"

        unk "Aku ambil jurusan informatikaa, karena dari aku kecil udah suka banget sama yang namanya ngoding"

        "...."

        "Dari kecil?"

        "Bahkan lingkunganku pun tidak pernah sekalipun menyebutkan istilah ngoding"

        mc "Wuihh keren... aku juga pengen ambil informatika juga nih"

        hide elisa netral2
        show elisa ketawa

        unk "Wahh bisa sama yaa, semoga bisa keterima yaa!"

        mc "Kamu juga. BTW boleh kenalan ga? kenalin aku [McName]"

        hide elisa ketawa
        show elisa netral2

        nr101 "Bolehh, halo [McName] kenalin aku Elisa"

        mc "Elisa... salam kenal ya"

        nr101 "Salam kenal juga!"
    elif ngobrol_r101 == 1:
        $ ngobrol_r101 += 1

        show elisa netral1

        mc "Ngomong-ngomong Lis, persiapan SNBT mu gimana aman kah?"

        hide elisa netral1
        show elisa netral2

        nr101 "Dari aku semoga aman ya, karena nilai TO ku udah bisa di atas passing grade walaupun agak mepet"

        mc "Wihh... udah pasti aman sih itu, kalau kata kakak kelasku yang lolos sih nilai SNBT nya selalu di
        atas nilai try out juga"

        mc "Bahkan yang waktu try out nilainya 500 terus, waktu SNBT nilainya bisa 700"

        show elisa ketawa

        nr101 "Wihh... sejauh itu naiknya? kalo gitu ngga perlu khawatir deh"

        hide elisa ketawa
        show elisa netral2

        mc "Iya semoga aman aja sih, btw nilai subtest tertinggi mu di subtest apa?"

        nr101 "Oh kalo aku tertinggi di Penalaran Matematika, karena aku sering ngerjain tugas ngoding
        jadi banyak tipe soal yang familiar di sini"

        hide elisa netral2
        show elisa ketawa

        nr101 "Jadi aku ngga perlu belajar banyak banyak ehe"

        "...."

        "Apakah ada korelasinya orang pintar sama suka matematika?"

        "Kenapa kebanyakan orang pintar yang kutemui selalu suka dengan matematika?"

        mc "Owhh menarik banget sih itu... ada tips ga buat bisa ningkatin nilai PM ku?"

        hide elisa ketawa
        show elisa netral1

        nr101 "Hmmm...."

        ".....?"

        hide elisa netral1
        show elisa netral2

        nr101 "Jujurly aku kurang tau ya gimana, karena aku sering ngerjain soal soal jadi mungkin dari aku
        banyakin latihan soal aja sihh"

        nr101 "Tapi terkadang kalo emang waktunya ngga sempet aku selalu nembak C"

        nr101 "Nilaiku masih selalu aman meskipun ada yang nembak"

        mc "Ohh... begitu ya, oke makasih sarannya"

        hide elisa netral2
        show elisa ketawa

        nr101 "You're welcome~"

        hide elisa ketawa
    elif ngobrol_r101 == 2:
        $ ngobrol_r101 += 1

        show elisa netral1

        mc "Ngomong-ngomong Lis, kalo udah keterima nanti rencanamu mau ngapain aja?"

        nr101 "Hmm....."

        "...?"

        hide elisa netral1
        show elisa netral2

        nr101 "Rencanaku sih pengen banyak banyakin ikut lomba sihh, sekalian ngasah logika sama skill
        ngodingku gitu. Nanti kalo menang kan bisa dapet cuan juga jadi win-win situation for me"

        mc "Ohh i see, rencanamu keren banget yak nanti bisa membanggakan nama almamater juga"

        mc "Kalo aku sih ya cuma pengen mbuat game aja sih, selain itu masih belum kepikiran"

        nr101 "Ohh bikin game? aku denger denger itu bikinnya susah banget lohh, kalo kamu bisa
        keren abiss sih..."

        mc "Iya karena aku suka banget main game apalagi yang punya Story sama Karakter yang bagus"

        mc "Tapi rasanya genre game seperti itu masih berasa nggak banyak orang yang tau"

        mc "Padahal game kayak gitu bisa punya nilai edukatif dan nilai seni loh"

        mc "Makanya aku pengen bikin game yang punya nilai edukatif dan gimana caranya biar semua orang
        itu bisa ngerasa senang mainin gameku"

        hide elisa netral2
        show elisa ketawa

        nr101 "Kerennn.... semangat ya!"

        mc "Sama-sama lis"

        hide elisa ketawa
    else:
        "Aku sudah kehabisan topik yang ingin kubicarakan"
    jump r101

label masjid:
    scene musholla dalam
    with fade
    if not places_discovered["masjid"]:
        $ places_discovered["masjid"] = True

        "Jadi ini mushollanya"

        "Tempatnya lumayan sejuk karena ada AC, tetapi tergolong kecil untuk fasilitas yang di mana jumlah mahasiswanya
        bisa sampai 1.000"

        "Oh di sini ada orang yang selesai sholat juga rupanya"

        "Dia kayaknya masih muda, apakah dia lagi ngesurvey lokasi SNBT juga?"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    menu:
        "Apa yang harus aku lakukan di sini?"
        "Ajak Ngobrol":
            jump ngobrol_di_masjid
        "Inspek":
            jump inspekMasjid
        "Keluar":
            jump r101

label inspekMasjid:
    "Musholla ini terlihat seperti musholla pada umumnya..."

    "Ada 3 shaf, dan ada tempat sendiri di paling depan untuk seorang imam."

    "Aku lihat di sebelah kanan imam juga ada semacam meja untuk mengaji"

    "Apakah di sini sering ada acara pengajian juga?"

    scene musholla dalam 2
    with fade

    "Di dekat pintu masuk ada banyak sekali laci yang aku tidak tahu apa isinya"

    "Tidak lupa dengan adanya kotak infaq juga"

    scene musholla wudhu

    "Dan jika aku keluar, di sebelah kanan dari musholla ini adalah tempat wudhunya"

    "Terlihat ada 6 keran untuk berwudhu, dan ada kolam ikan juga?"

    "Woh bisa ngasih minum ikannya nih kalo mereka haus"

    jump masjid

label ngobrol_di_masjid:
    if ngobrolMasjid == 0:
        $ ngobrolMasjid += 1

        "Aku mencoba mengajak ngobrol anak itu"

        mc "Permisi mas, masnya survey lokasi SNBT kah?"

        show gilang kaget

        unk "Oh iya mas, ini saya barusan selesai jadi sekalian sholat dhuhur dulu sebelum balik"

        mc "Eh sudah waktunya dhuhur ya? jujur ngga kedengeran adzan dari tadi"

        hide gilang kaget
        show gilang netral

        unk "Iya mas kebetulan saya ngecek jam di hp saya udah waktunya dhuhur"

        mc "Ohh oke oke, btw mau kuliah di ITS juga kah mas?"

        unk "Oh nggak mas ini saya survey buat adik saya karena dia lupa belum survey, trus hari ini
        juga dia ada acara jadi ngga bisa survey"

        mc "Oalah begitu ya mas, berarti sekarang masnya udah kuliah?"

        unk "Iya aku udah kuliah di Teknik Industri UB lewat SNBP"

        mc "SNBP? wah nilai rata ratanya tinggi pasti ya mas"

        unk "Ah ngga juga sih, cuma rata rata 90"

        "...."

        "90 ngga tinggi?"

        "Orang pinter standarnya beda banget yak sama orang pas pasan kayak aku ini"

        mc "Wih lumayan sih itu mas, ngga kaget pasti kalo diterima. BTW boleh kenalan ga? kenalin aku [McName]"

        nmasjid "Boleh mas, aku Gilang"

        mc "Salam kenal Gilang"

        nmasjid "Salam kenal juga"

        hide gilang netral
    elif ngobrolMasjid == 1:
        $ ngobrolMasjid += 1

        mc "Btw masnya pernah nyoba try out SNBT gitu ga mas?"

        show gilang netral

        nmasjid "Pernah"

        hide gilang netral
        show gilang ketawa

        nmasjid "Tapi ngga lolos passing grade"

        hide gilang ketawa
        show gilang netral

        mc "Oh, mau ambil jurusan mana mas waktu SNBT, Tekdus juga kah?"

        nmasjid "Ngga..."

        hide gilang netral
        show gilang ketawa

        nmasjid "Aku waktu itu ngambilnya Kedokteran UI"

        "Ehh.... pantes aja"

        "Meskipun 600 atas pun masih belum lolos passing grade itu"

        mc "Waduh langsung nyoba final boss ya mas, tapi kok sekarang kuliahnya di TekDus mas?"

        hide gilang ketawa
        show gilang netral

        nmasjid "Karena desakan ortu aja"

        nmasjid "Kebetulan ortu ku ada yang kerja di bagian industri"

        nmasjid "Jadi aku ada sedikit-sedikit pengetahuan nanti"

        mc "Oalah, ngga lolos passing grade itu berapa mas emangnya?"

        nmasjid "Sekitar 630an kalo ga salah"

        mc "Wuih gede juga sih itu, ada saran ga mas biar bisa dapet nilai segitu?"

        nmasjid "Hmm... gimana ya, aku bagus di PBM sih nah kuncinya biar bisa cepet nyelesaiin soal PBM
        itu nerapin konsep yang namanya skimming sama scanning, mungkin bisa cari tau aja contoh soal
        yang skimming itu bagaimana dan scanning itu yang bagaimana"

        nmasjid "Tapi kalo misal waktunya ngga sempet ya aku nembak A"

        mc "Oh begitu ya mas, oke makasih"

        nmasjid "Sama-sama mas"

        hide gilang netral
    elif ngobrolMasjid == 2:
        $ ngobrolMasjid += 1

        mc "Btw rencananya waktu kuliah gimana mas?"

        show gilang kaget

        nmasjid "Hmm......"

        hide gilang kaget
        show gilang ketawa

        nmasjid "Belum tau sih mas, ngikut alur aja aku"

        hide gilang ketawa
        show gilang netral

        mc "Waduh okedeh, kalo aku sih kan pengen masuk informatika ITS ya,
        jadi nanti rencanaku bikin kayak game gitu"

        hide gilang netral
        show gilang kaget

        nmasjid "Bikin game? wih aku juga seneng main game nih mas, ntar kalo udah bikin infoin yak"

        hide gilang kaget
        show gilang netral

        mc "Amiin makasih mas"

        hide gilang kaget
    else:
        "Aku sudah tidak tahu topik apalagi yang ingin kubicarakan"

    jump masjid

label diParkiran:
    scene parkiran
    with fade
    if not places_discovered["parkiran"]:
        $ places_discovered["parkiran"] = True

        "Ternyata ini adalah parkiran motor"

        "Tidak ada yang spesial, hanya tempat untuk memarkirkan motor mahasiswa dan dosen"

        mc "Andaikan aku bisa naik motor, pasti ngga perlu keluar banyak duit buat pesen ojek online"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    else:
        "Ini hanya tempat memarkirkan motor"

    menu:
        "Apa yang harus aku lakukan di sini?"
        "Masuk":
            jump diGedung2
        "Ke belakang gedung Informatika" if visited_parkiran_via_r101 == 1:
            jump r101
        "Kembali":
            jump diDepanTC

label lt2:
    scene lantai2
    with fade
    if not places_discovered["lt2"]:
        $ places_discovered["lt2"] = True

        "Aku sampai di lantai 2"

        "Yang pertama kali menarik perhatianku adalah papan madingnya"

        "Banyak sekali jenis jenis lomba yang bisa diikuti oleh mahasiswa di sini"

        mc "Ada CTF, Hackathon, Competitive Programming..."

        "Aku tidak tau maksud kebanyakan dari jenis jenis lomba yang tertulis"

        "Tetapi itu artinya mereka yang bisa memenangkan lomba itu adalah orang yang sangat hebat bukan?"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    
    menu:
        "Apa yang harus aku lakukan di sini?"
        "Inspek":
            jump inspekLt2
        "Maju Kiri" if not places_discovered["tu"]:
            jump keTU
        "Ke lorong TU" if places_discovered["tu"]:
            jump keTU
        "Maju Kanan" if not places_discovered["aula"]:
            jump keAula
        "Ke lorong Aula" if places_discovered["aula"]:
            jump keAula
        "Naik Tangga":
            scene tangga_naik
            "Aku menaiki tangga..."
            jump lt3
        "Turun Tangga":
            scene tangga_turun
            "Aku menuruni tangga..."
            jump diGedung1

label inspekLt2:
    "Tidak banyak yang bisa kulihat di sini..."

    "Selain mading itu, ada juga peta lokasi yang terletak di dinding"

    "Peta tersebut hanya menunjukkan kode kode kelas"

    "..."

    "Aku tidak menemukan ruang LP2"

    "Apakah ini peta lama atau memang LP2 punya kode sendiri?"

    "Kemudian aku mencoba melihat sekelilingku lagi"

    scene microsoft
    with fade

    "...."

    "Ada ruang microsoft?"

    "Di sini tertulis mobility lab, aku tidak tahu apa maksudnya"

    "Apakah di sini lab untuk mengembangkan aplikasi mobile?"

    jump lt2

label keTU:
    scene ruang_tu
    with fade
    if not places_discovered["tu"]:
        $ places_discovered["tu"] = True
        "Aku pergi ke arah kiri..."

        "Kemudian ada orang keluar dari ruang yang kulihat tulisannya merupakan Ruang TU"

        "Orang itu berjalan mendekatiku"

        show bapak bapak tu

        bpk "Maaf mas ini sedang ada meeting jadi masnya dimohon jangan lewat dulu nggih"

        mc "Oh iya pak"

        hide bapak bapak tu

        "Ada meeting?"

        "Kenapa ngga boleh lewat, emangnya meetingnya di luar?"

        "Ya sebaiknya aku patuhi kata-kata bapak itu supaya aku tidak diusir"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"

        jump lt2
    else:
        "Aku tidak bisa melewati lorong ini"

        jump lt2

label keAula:
    scene ruang_aula
    with fade
    if not places_discovered["aula"]:
        $ places_discovered["aula"] = True

        "Aku pergi ke arah kanan..."

        "Kemudian ada orang keluar dari ruangan yang nampaknya tertulis \"Aula\""

        "Orang itu berjalan mendekatiku"

        show bapak bapak aula

        bpka "Maaf mas di Aula lagi ada shooting seminar orang tua mahasiswa, dimohon masnya
        tidak lewat sini nggih"

        mc "Oh iya pak"

        hide bapak bapak aula

        "Waduh kayaknya lagi ada acara"

        "Mending aku ikutin kata bapaknya aja deh daripada diusir"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"

        jump lt2
    else:
        "Aku tidak bisa melewati lorong ini"

label lt3:
    scene lt3
    with fade
    if not places_discovered["lt3"]:
        $ places_discovered["lt3"] = True

        "Aku sampai di Lantai 3"

        "..."

        "Wah"

        "Tempat ini sudah seperti salon yang sangat di luar jangkauanku"

        mc "Orang luar kalo pengen belajar gitu boleh ga ya belajar di sini?"

        "Vibe yang dipancarkan oleh tempat ini benar benar bisa bikin santai."

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"

    menu:
        "Apa yang harus aku lakukan di sini?"
        "Inspek":
            jump inspekLt3
        "Maju Kiri" if not places_discovered["lp2"]:
            "Aku bergerak ke arah depan kiri..."
            jump lp2
        "ke LP2" if places_discovered["lp2"]:
            "Aku masuk ke LP2..."
            jump lp2
        "Maju Kanan" if not places_discovered["laboratorium_giga"]:
            jump labgiga
        "Ke lorong lab IGS" if places_discovered["laboratorium_giga"]:
            jump labgiga
        "Turun tangga":
            scene tangga_turun
            "Aku menuruni tangga...."
            jump lt2

label inspekLt3:
    "Tidak banyak yang bisa ku lihat di sini"

    "Selain dari tempat belajar yang layaknya salon mewah, ada meja besar yang tersandar di sebelah toilet"

    "Meja apa itu kira-kira? dari ukurannya sih menurutku seperti meja untuk olahraga Tenis Meja"

    "Jika warga di sini menyimpan meja tenis di sini, apakah di sini sering ada ajang tenis meja?"

    jump lt3

label labgiga:
    scene lab_giga
    with fade
    if not places_discovered["laboratorium_giga"]:
        $ places_discovered["laboratorium_giga"] = True

        "Aku pergi ke arah kanan..."

        "Kemudian ada orang keluar dari ruangan yang nampaknya tertulis Lab Interaksi, Grafika, dan Seni"

        "Lab untuk apa itu kira kira?"

        "Orang itu berjalan mendekatiku"

        show mas mas hengker

        mmh "Maaf mas di lorong ini lagi ada shooting film mahasiswa henger, dimohon masnya
        tidak lewat lorong sebelah sini ya"

        mc "Oh iya mas"

        hide mas mas hengker

        "Wah shooting film?"

        "Mending aku ngga lewat sini dulu sih biar ngga ngganggu proses shootingnya"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    else:
        "Aku tidak bisa melewati lorong ini"
    jump lt3

label lp2:
    if not places_discovered["lp2"]:
        $ places_discovered["lp2"] = True

        "Aku melewati beberapa lorong yang tampaknya berisikan beberapa lab"

        "Lab algoritma pemrograman... Lab Pemrograman 2..."

        mc "Bentar..."

        mc "Lab Pemrograman 2?"

        mc "Kalau disingkat berarti jadi Lp2?"

        "Aku akhirnya mencoba masuk ke dalam ruangan itu"

        scene lp2
        with fade

        "Yap ternyata benar"

        "Ini adalah lokasi aku melaksanakan SNBT ku nanti"

        "Aku tahu karena ada tulisan angka di atas monitor komputernya yang menandakan angka tempat duduk"

        mc "Oh ternyata ada yang udah dateng duluan"

        "Dari kejauhan terlihat ada cewek yang sedang browsing di komputer lab ini"

        "Apakah dia mahasiswa atau anak yang sedang survey juga?"

        if discovered_all_places():
            "Kurasa aku sudah mengunjungi semua tempat di sini"

            "Aku masih bisa melanjutkan eksplorasi dan pulang dengan cara pesan ojek online di depan gedung Informatika"

            menu:
                "Apakah aku ingin pulang sekarang?"
                "Ya":
                    "Baiklah, Saatnya pulang dan bersiap untuk hari yang dapat mengubah hidupku"

                    jump hariUTBK
                "Tidak":
                    "Aku masih ingin eksplorasi lagi tempat ini"

                    "Barangkali ada hal yang terlewat atau aku ingin ngobrol dengan anak-anak di sini"
    else:
        scene lp2
        with fade

    menu:
        "Apa yang harus aku lakukan di sini"
        "Ajak ngobrol":
            jump ngobrol_di_lp2
        "Inspek":
            jump inspekLp2
        "Keluar":
            "Aku keluar dari ruangan..."
            jump lt3

label inspekLp2:
    if inspectedLp2 == 0:
        $ inspectedLp2 += 1

        "Aku melihat-lihat sekelilingku...."

        "Laboratorium pemrograman...."

        "Sudah pasti hanya ada komputer di sini"

        "Maksudku tidak mungkin mereka membuat program dengan cara menulis di kertas kan?"

        "Aku mencoba menyalakan salah satu komputernya..."

        "...."

        "Tidak ada respon?"

        "Apakah ada mekanisme tersendiri supaya komputer ini tidak dinyalakan oleh sembarangan orang?"
    elif inspectedLp2 == 1:
        $ inspectedLp2 += 1

        "Aku mencoba menyalakannya lagi..."

        "...."

        "Masih tidak ada tanda kehidupan"

        "Mungkin memang ada mekanisme sendiri supaya dapat menyala?"
    elif inspectedLp2 == 2:
        $ inspectedLp2 += 1

        "Aku mencoba menyalakannya lagi, kali ini aku coba menekan lebih keras pada tombol powernya"

        "...."

        "Oh indikator lampunya sudah menyala"

        "Sudah berapa kali komputer ini digunakan sehingga tombol powernya sulit ditekan?"

        "Sebagai ritual tersendiri terhadap komputer yang aku temui, aku mencoba membuka task manager untuk
        melihat spesifikasinya"

        "Intel I7 12th gen....."

        "Sudah kuduga kalau komputer pemrograman seharusnya menggunakan processor yang cepat"

        "Dengan processor seperti ini, aku tidak perlu khawatir waktuku habis menunggu komputer yang tidak merespon"

        "Aku pun mematikan kembali komputer tersebut"
    else:
        "Sudah tidak ada lagi yang bisa aku lihat"

    jump lp2

#Unfinished
label ngobrol_di_lp2:
    if ngobrolLp2 == 0:
        $ ngobrolLp2 += 1

        mc "Aku mencoba ngajak ngobrol anak itu..."

        mc "Halo mbak, mbaknya survey lokasi SNBT juga kah?"

        unk "Iya"

        mc "Oh berarti ngerjain di sini juga ya?"

        unk "Iya"

        mc "Sama nih, boleh kenalan ga?"

        nlp2 "Aku Farah"

        mc "Salam kenal Farah, aku [McName]"

        nlp2 "Salam kenal juga [McName]"
    elif ngobrolLp2 == 1:
        $ ngobrolLp2 += 1

        mc "Btw persiapan SNBT gimana aman kah?"

        nlp2 "Literasi BIndo nembak C udah"

        nlp2 "Dijamin nilainya gede"

        mc "Oh berarti aman ya?"

        nlp2 "..."

        "Dia tidak menjawab"

        "Mungkin anak ini agak introvert"

        "Aku sebaiknya tidak mengganggunya"
    else:
        "Aku tidak punya topik lagi untuk kubicarakan"

    jump lp2

# Unfinished
label hariUTBK:
    $ renpy.music.set_volume(0.0, delay=1, channel='music')
    scene black
    with fade
    $ renpy.pause(1.0, hard=True)
    stop music
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    "Kring....."
    "Alarm berbunyi nyaring..."
    scene kamar with fade
    mc "woahh... hari ini hari-H UTBK..."
    if eksplor == 1:
        mc "Untung kemarin aku udah survey jadi udah tau lokasinya"
    menu:
        "Bangun dan siap-siap":
            jump bangun
        "Tidur lagi bentar...":
            mc "Hmm... tidur lagi bentar ah"
            mc "5 menit lagi bangun deh"
            jump bangun

label bangun:
    scene kamar with fade
    mc "Akhirnya bangun juga..."
    mc "Sekarang saatnya siap-siap"
    mc "Semoga hari ini berjalan lancar..."
    "Kamu bergegas mandi dan mengenakan pakaian yang nyaman."
    "Sarapan kilat sudah menanti di meja."
    "Setelah selesai, kamu meraih tas berisi dokumen dan alat tulis."

label tiba_tc:
    scene tc_depan
    with fade
    mc "Wahh udah sampe di TC"
    mc "Sekarang saatnya ngerjain UTBK"
    mc "Semoga hasilnya memuaskan ya"
    "Kamu melangkah masuk ke dalam gedung dengan penuh semangat."
    "Terlihat banyak calon peserta UTBK lain yang juga baru tiba."
    "Kamu pun langsung menuju ruang ujian yang sudah ditentukan."

    scene depan_ruang with fade
    mc "Wahh udah sampe di ruang ujian"
    show satpam at left
    "Di depan pintu ruangan, seorang satpam berdiri tegap."
    satpam "Selamat pagi, silakan tunjukkan kartu peserta dan kartu identitas Anda."
    mc "Selamat pagi, Pak. Ini kartu saya."
    "Kamu menyerahkan kedua kartu kepada satpam."
    satpam "Terima kasih. Sekarang, mohon buka tas Anda, kami akan melakukan pemeriksaan barang bawaan."
    menu:
        "Membuka tas dan menunjukkan isinya dengan tenang.":
            mc "Tentu, Pak. Ini isinya."
            "Kamu membuka tas, memperlihatkan alat tulis, botol air minum transparan, dan dokumen-dokumen penting."
            satpam "Baik, tidak ada barang yang mencurigakan. Silakan."
            jump masuk_ruangan
        "Sedikit panik tapi tetap mengikuti arahan.":
            mc "(Aduh, jangan sampai ada yang ketinggalan atau salah...)"
            "Dengan sedikit gemetar, kamu membuka tas dan menunjukkan isinya."
            satpam "Semua sesuai. Silakan masuk."
            jump masuk_ruangan
        "Berusaha menyembunyikan sesuatu (Mungkin ide buruk?).":
            mc "(Jangan sampai ketahuan kalau aku bawa...)"
            "Kamu mencoba sedikit menggeser sesuatu di dalam tas agar tidak terlihat."
            satpam "Maaf, mohon perlihatkan semua isi tas Anda dengan jelas."
            "Kamu terpaksa menunjukkan semuanya."
            # Di sini bisa ada konsekuensi jika MC mencoba menyembunyikan barang terlarang
            jump masuk_ruangan # Untuk sementara kita langsung masuk ruangan

label masuk_ruangan:
    scene lp2 with fade
    "Kamu memasuki ruangan ujian."
    "Suasana terasa tegang namun penuh harapan."
    mc "Akhirnya... saatnya mengerjakan."

    scene lp2 with fade
    "Subtest 1: Penalaran Umum"

    menu:
        "j = 5\nonpf xfyz inyfrgfm xfyz fifqfm izf1 rfpf izf inyfrgfm izf fifqfm"
        "tzozm":
            "Apakah benar ini jawabannya?"
        "erufy":
            "Apakah benar ini jawabannya?"
            $ correctAnswer += 1
        "lnrfm":
            "Apakah benar ini jawabannya?"
        "sfyzz":
            "Apakah benar ini jawabannya?"
        "tnlff":
            "Apakah benar ini jawabannya?"
        
    scene lp2 with fade
    "Subtest 2: Pengetahuan & Pemahaman Umum"

    show ppu

    menu:
        "Perumpamaan dalam teks tersebut terdapat pada kalimat ...."
        "1":
            "Apakah benar ini jawabannya?"
        "3":
            "Apakah benar ini jawabannya?"
        "7":
            "Apakah benar ini jawabannya?"
        "6":
            "Apakah benar ini jawabannya?"
        "4":
            "Apakah benar ini jawabannya?"
            $ correctAnswer += 1

    hide ppu

    scene lp2 with fade
    "Subtest 3: Kemampuan Memahami Bacaan & Menulis"

    show kmbm

    menu:
        "Perumpamaan dalam teks tersebut terdapat pada kalimat ...."
        "8":
            "Apakah benar ini jawabannya?"
            $ correctAnswer += 1
        "7":
            "Apakah benar ini jawabannya?"
        "6":
            "Apakah benar ini jawabannya?"
        "5":
            "Apakah benar ini jawabannya?"
        "4":
            "Apakah benar ini jawabannya?"
    
    hide kmbm

    scene lp2 with fade
    "Subtest 4: Pengetahuan Kuantitatif"

    show pk

    menu:
        "Apa jawabannya?"
        "SEMUA pilihan benar":
            "Apakah benar ini jawabannya?"
        "1, 2, dan 3 SAJA yang benar":
            "Apakah benar ini jawabannya?"
            $ correctAnswer += 1
        "2 dan 4 SAJA yang benar":
            "Apakah benar ini jawabannya?"
        "HANYA 4 saja yang benar":
            "Apakah benar ini jawabannya?"
        "1 dan 3 SAJA yang benar":
            "Apakah benar ini jawabannya?"

    hide pk

    scene lp2 with fade
    "Subtest 5: Literasi Dalam Bahasa Indonesia"

    show bindo

    menu:
        "Apa jawabannya?"
        "A":
            "Apakah benar ini jawabannya?"
        "B":
            "Apakah benar ini jawabannya?"
        "C":
            "Apakah benar ini jawabannya?"
            $ correctAnswer += 1
        "D":
            "Apakah benar ini jawabannya?"
        "E":
            "Apakah benar ini jawabannya?"

    hide bindo

    scene lp2 with fade
    "Subtest 6: Literasi Dalam Bahasa Inggris"

    show bing

    menu:
        "What does the passage mainly talk about?"
        "Controlling the habit of using fabric softener":
            "Apakah benar ini jawabannya?"
        "The popularity of fabric softener in the US":
            "Apakah benar ini jawabannya?"
        "Harmful compounds found in fabric softener":
            "Apakah benar ini jawabannya?"
        "The downside of fabric softener usage":
            "Apakah benar ini jawabannya?"
            $ correctAnswer += 1
        "Environmental issues caused by fabric softener":
            "Apakah benar ini jawabannya?"

    hide bing

    scene lp2 with fade
    "Subtest 7: Penalaran Matematika"

    show pm

    menu:
        "Apa Jawabannya?"
        "950":
            "Apakah benar ini jawabannya?"
        "2.250":
            "Apakah benar ini jawabannya?"
        "1.300":
            "Apakah benar ini jawabannya?"
            $ correctAnswer += 1
        "475":
            "Apakah benar ini jawabannya?"
        "825":
            "Apakah benar ini jawabannya?"
    
    scene kamar
    with fade
    if correctAnswer < 0:
        jump bad_ending
    if correctAnswer > 1 and correctAnswer <= 7:
        jump good_ending
    if correctAnswer == 7 and eksplor == 1:
        jump best_ending

label bad_ending:
    "Aku gagal lolos ke Informatika ITS karena hanya berhasil menjawab [correctAnswer] soal"

    "Bad ending"

    return

label good_ending:
    "Aku lolos ke Informatika ITS karena berhasil menjawab [correctAnswer] soal"

    "Good ending"

    return

label best_ending:
    "Aku lolos ke Informatika ITS dengan nilai SNBT tertinggi karena berhasil menjawab semua soal dan
    melakukan eksplorasi kampus"

    "Best ending"

    return