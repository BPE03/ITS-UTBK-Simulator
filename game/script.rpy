# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[McName]")
define unk = Character("???")
define nbun = Character("Cynthia")
define nr101 = Character("Farah")
define nr105 = Character("Andi")
define nr109 = Character("Billy")
define nlp2 = Character("Elisa")
define nkantin = Character("Danan")
define nmasjid = Character("Gilang")
define audio.c1 = "<loop 21.44>audio/Sun_Rays.wav"

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

    scene bundaran_ITS
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
    "INi di depan tc"

    return

label hariUTBK:
    "Ini hari utbk"

    return