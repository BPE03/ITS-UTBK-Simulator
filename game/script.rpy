# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[McName]")
define unk = Character("???")
define bpk = Character("Bapak Bapak TU")
define bpka = Character("Bapak Bapak Aula")
define mmh = Character("Mas Mas hengker")
define nbun = Character("Cynthia")
define nr101 = Character("Farah")
define nr105 = Character("Andi")
define nr109 = Character("Billy")
define nlp2 = Character("Elisa")
define nkantin = Character("Danan")
define nmasjid = Character("Gilang")
define audio.c1 = "<loop 21.44>audio/Sun_Rays.wav"
define satpam = Character("Satpam")

default eksplor = 0
default inspectedBundaran = 0
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

    unk "Oh ya, FSM dari game ini dapat di lihat di gambar berikut"

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

    hide eileen happy

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

                        nbun "Okeeyy hati-hati ya!"

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

        unk "...."

        "Ah ga dijawab lagi, apa aku salah mulainya ya?"

        mc "halo mbak?"

        unk "Eh iya mas, ada apa ya?"

        mc "Oh ngga tadi aku liat mbaknya lagi foto-foto kampusnya tadi, pengen kuliah di sini kah mbak?"

        unk "Iya mas, sekalian survey lokasi SNBT juga"

        mc "Loh sama nih, aku juga pengen kuliah di ITS juga, SNBT nya juga ngerjain di ITS. ngomong ngomong
        mau masuk jurusan mana mbak?"

        unk "Aku pengennya masuk Teknologi Kedokteran sih pilihan pertamanya, ya tapi kalo ngga dapet
        pilihan kedua ku di Teknik Kimia. Kalo masnya ambil jurusan apa?"

        mc "Aku sih ngambil Teknik Informatika di pilihan pertamanya, pilihan keduanya jujur ngga tau haha,
        tapi yang mirip mirip sih di Sistem Informasi jadi itu pilihan kedua ku."

        unk "Wihh kerenn..... yakin lolos mas? itu keduanya passing-gradenya tinggi banget loh"

        mc "Harus yakin dong, kalo ga yakin gimana bisa lolos kalo mentalnya down duluan? dari SD sampe SMA
        aku selalu percaya diri meskipun masih ada materi yang belum aku bener bener pahami."

        mc "Kalo udah yakin, mentalnya tenang, pasti waktu ngerjain juga bakal dateng dengan sendiri ilmunya"

        "Aku ngomong begitu dengan pedenya"

        "Padahal mah aku selalu beruntung aja bisa dapet nilai sesuai ekspektasi"

        "Emang aku bisa lolos di jurusan dengan peminat terbanyak hanya ngandelin beruntung doang?"

        unk "Wih bener banget sih itu, semoga lolos ya mas"

        mc "Amiin kamu juga ya. BTW boleh kenalan ga?"

        nbun "Boleh mas, kenalin aku Cynthia"

        mc "Cynthia... kenalin aku [McName]. Salam kenal ya"

        nbun "Salam kenal juga"

    elif ngobrolBundaran == 1:

        $ ngobrolBundaran += 1

        mc "BTW Cynthia, persiapan SNBT mu gimana aman ga?"

        nbun "Alhamdulillah liat hasil Try-Out ku yang selalu di atas passing grade, aku optimis sih
        bisa lolos. Kalo kamu gimana?"

        mc "Yaa.... aku udah nyoba pelajarin hasil try out ku yang hasilnya kayak uang koin itu....
        ya semoga beruntung aja sih, biasanya kurang bisa mikir cepat aku walaupun udah paham soalnya"

        nbun "uang koin berapa mas? 100? 200?"

        "Buset dia ketawa lagi."

        "Jadi malu aku, hasil TO nya dia dah aman banget, lah aku hasil pas pasan gini malah sok ngasih
        kata kata motivasi"

        mc "Kalo nilaiku segitu udah aku buang jauh jauh sih koin sama harapanku"

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

        nbun "Sama-sama mas"

    elif ngobrolBundaran == 2:
        $ ngobrolBundaran += 1

        mc "Btw kalo misal kamu ga lolos SNBT gimana Cyn?"

        nbun "Loh kok tanya gitu, katanya tadi harus yakin?"

        mc "Bener yakin itu penting, tapi tetep aja ngga menutupi worst casenya juga kan, karena
        aku juga bingung kalo ngga lolos nanti harus gimana lagi"

        mc "Mandiri? darimana duitnya, gap year? ya mungkin pilihan terbaikku buat belajar lebih banyak lagi"

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

        nbun "Okeyy~"

    elif ngobrolBundaran == 3:
        $ ngobrolBundaran += 1

        mc "Btw kalo udah lolos ITS nanti rencananya mau ngapain aja?"

        nbun "Belum tau sih mas, yang pasti aku pengen nyoba ikut riset kalo ada, 
        atau pengen nyoba teoriku yang lagi aku kembangin yaitu bikin alat untuk ngobatin kanker"

        "...."

        "Kalo aku bilang dia jenius kayaknya masih kurang deh"

        mc "Kamu udah bikin penelitian sendiri?"

        nbun "Iya, tapi karena ngga ada fasilitasnya jadi aku ngga bisa nyoba, makanya aku pengen banget
        buat lolos ke jurusan ini"

        "Ya aku hanya berharap kamu tidak ada di pesawat aja"

        mc "Aku ngga tau sih mau ngomong apa lagi"

        mc "Rasanya apapun rencana yang mau aku ceritain kaya ngga ada apa apanya haha"

        nbun "Gapapa mas cerita aja, ngga adil dong kan aku udah cerita masa kamu ngga"

        mc "Waduh oke deh, jadi rencanaku setelah masuk ke Informatika itu ya pengen nyoba bikin game gitu"

        nbun "Oh masnya suka main game kah?"

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

        nbun "Jujur aku ngga tau apa apa tentang game mas, tapi apapun rencana masnya semoga bisa kecapai ya"

        mc "Kamu juga Cyn."

    else:
        mc "Aku tidak tau topik apalagi yang ingin kubicarakan"

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

# Unfinished
label ngobrol_di_kantin:
    "ngobrol kantin"

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

        "Inspek":
            jump inspekGedung1

        "Keluar":
            "Aku keluar dari sini..."
            jump diDepanTC
    return

# Unfinished
label inspekGedung1:
    "Inspek"
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
    "ngobrol"

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

#Unfinished
label ngobrol_di_r106:
    "Ngobrol"

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
        "Naik Tangga":
            jump mau_ke_lt2
        "Inspek":
            jump inspekGedung2
        "Maju kiri" if not places_discovered["r106"]:
            "Aku pergi ke arah kiri depan..."
            jump r106
        "Ke lorong Ruang 106-108" if places_discovered["r106"]:
            "Aku pergi ke lorong ruang 106-108..."
            jump r106
        "Maju kanan" if not places_discovered["r101"]:
            "Aku pergi ke arah kanan depan..."
            jump r101
        "Ke lorong Ruang 106-108" if places_discovered["r101"]:
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

#unfinished
label inspekGedung2:
    "Inspek gedung 2"

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

#unfinished
label ngobrol_di_r101:
    "Ngobrol"
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

#Unfinished
label inspekMasjid:
    "Inspek masjid"

    jump masjid

#Unfinished
label ngobrol_di_masjid:
    "Ngobrol di masjid"

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
        "Maju Kiri":
            jump keTU
        "Maju Kanan":
            jump keAula
        "Naik Tangga":
            scene tangga_naik
            "Aku menaiki tangga..."
            jump lt3
        "Turun Tangga":
            scene tangga_turun
            "Aku menuruni tangga..."
            jump diGedung1

#Unfinished
label inspekLt2:
    "Inspek"

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
        "Maju Kiri":
            "Aku bergerak ke arah depan kiri..."
            jump lp2
        "Maju Kanan":
            jump labgiga
        "Turun tangga":
            scene tangga_turun
            "Aku menuruni tangga...."
            jump lt2

#Unfinished
label inspekLt3:
    "Inspek"

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

        mmh "Maaf mas di Aula lagi ada shooting film mahasiswa henger, dimohon masnya
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

#unfinished
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

#unfinished
label inspekLp2:
    "Inspek"

    jump lp2

#Unfinished
label ngobrol_di_lp2:
    "Ngobrol"

    jump lp2

# Unfinished
label hariUTBK:
    scene black
    "Kring....."
    "Alarm berbunyi nyaring..."
    scene kamar with fade
    mc "woahh... hari ini hari-H UTBK..."
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