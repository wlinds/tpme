import pickle
# This should be zipped/compressed in other format, as of now it works but it's messy
# maybe pickle it? but the end goal is to not use this bucket structure at all, might as well keep it for now

m_sweden_gpt = ["Lars", "Anders", "Johan", "Karl", "Per", "Mikael", "Jan", "Henrik", "Björn", "Erik", "Ingvar", "Hans", "Gustaf", "Nils", "Sven", "Olof", "Tomas", "Bo", "Urban", "Stig", "Lennart", "Ruben", "Kjell", "Emil", "Oskar", "Rolf", "Fredrik", "Magnus", "Jakob", "Petter", "Andreas", "Daniel", "Pelle", "Mathias", "Jonathan", "Viktor", "Isak", "David", "Anton", "Emilio", "Joel", "Adam", "Robin", "Leif", "Max", "Filip", "Alexander", "Martin", "William", "Göran", "Carl", "Mats", "Samuel", "Peder", "Thomas", "John", "Staffan", "Markus", "Gustav", "Bengt", "Jens", "Richard", "Jim", "Mattias", "Patrik", "Jörgen", "Olivia", "Stefan", "Christoffer", "Jimmie", "Marcus", "Elias", "Maurice", "Ulf", "Christian", "Håkan", "Marcus", "Gunnar", "Bertil", "Tobias", "Ingemar", "Mikael", "Linus", "Dennis", "Alfred", "Hans", "Sebastian", "Arne", "Jesper", "Janne", "Christer"]
f_sweden_gpt = ["Maria", "Anna", "Margareta", "Elisabeth", "Eva", "Birgitta", "Ingrid", "Karin", "Kristina", "Lena", "Marianne", "Inger", "Greta", "Annika", "Ulla", "Gunilla", "Lilian", "Astrid", "Sofia", "Agneta", "Yvonne", "Monica", "Elvira", "Ingegerd", "Bodil", "Annie", "Linn", "Ester", "Carina", "Sara", "Helena", "Emma", "Therese", "Lise-Lotte", "Kicki", "Lillemor", "Lottie", "Henny", "Lena", "Maud", "Jenny", "Lissie", "Livia", "Loulou", "Luna", "Linda", "Anita", "Lotta", "Louise", "Gunvor", "Linnea", "Inga", "Irene", "Stina", "Liv", "Mimmi", "Madeleine", "Maj-Britt", "Anette", "Mona", "Pia", "Inger", "Fanny", "Gudrun", "Barbro", "Ann-Sofie", "Charlotte", "Hanna", "Ida", "Rut", "Anna-Lena", "Ellen", "Cecilia", "Ebba", "Anita", "Linda", "Maj", "Frida", "Tova", "Viktoria", "Camilla", "Emilia", "Marta", "Nina", "Märta", "Maja", "Amanda", "Rebecca", "Julia", "Johanna"]
f_norwa_list = ['Nora', 'Norah', 'Emma', 'Ella', 'Maja', 'Maia', 'Maya', 'Olivia', 'Emilie', 'Sofie', 'Sophie', 'Leah', 'Sofia', 'Sophia', 'Ingrid', 'Frida', 'Sara', 'Sarah', 'Zara', 'Tiril', 'Selma', 'Ada', 'Hedda', 'Amalie', 'Anna', 'Alma', 'Hanna', 'Eva', 'Mia', 'Thea', 'Live', 'Ida', 'Astrid', 'Ellinor', 'ilde', 'Linnea', 'Iben', 'Aurora', 'Mathilde', 'Mathilde', 'Saga', 'Solveig', 'Marie', 'Eline', 'Oline', 'Maria']

m_scandi_gpt = ["Oliver", "Noah", "William", "Emil", "Liam", "Elias", "Oskar", "Axel", "Lucas", "Filip",
"Erik", "Isak", "Mikael", "Jakob", "Leo", "Simon", "Theodor", "Viktor", "Sebastian", "Alexander",
"Hampus", "Hugo", "Adrian", "Max", "David", "Fredrik", "Linus", "Edward", "Olle", "Arvid",
"Carl", "Henrik", "Kevin", "Elvin", "Nils", "Joel", "Magnus", "Daniel", "Mathias", "Anton",
"Linus", "Andreas", "Sondre", "Gustav", "Niklas", "Hannes", "Emilio", "Johan", "August", "Aron",
"Vemund", "Jens", "Markus", "Björn", "Johannes", "Viggo", "Ludvig", "Rasmus", "Benjamin", "Isac",
"Tomas", "Mats", "Eirik", "Olav", "Peder", "Kai", "Sander", "Anders", "Stian", "Even",
"Eirik", "Sverre", "Jakob", "Johan", "Tommy", "Truls", "Espen", "Marius", "Krister", "Geir"]

f_scandi_gpt = ["Emma", "Sofia", "Ella", "Maja", "Aurora", "Linn", "Nora", "Ida", "Molly", "Hanna",
"Lena", "Alma", "Violet", "Ingrid", "Frida", "Emilia", "Leah", "Livia", "Signe", "Linnea",
"Amanda", "Evy", "Tuva", "Thea", "Sara", "Camilla", "Julia", "Elise", "Amalie", "Eline",
"Ada", "Marie", "Emma", "Sofie", "Johanna", "Mia", "Ester", "Isabelle", "Martine", "Inger",
"Karoline", "Maria", "Ragnhild", "Synne", "Silje", "Annie", "Ingrid", "Tiril", "Eli", "Iben",
"Marte", "Andrea", "Tonje", "Rikke", "Anette", "Lise", "Elina", "Ellen", "Stine", "Ingvild",
"Helene", "Karen", "Guro", "Sandra", "Marianne", "Maren", "Turid", "Lene", "Bente", "Anne",
"Ingrid", "Bodil", "Grete", "Rita", "Astrid", "Berit", "Kari", "Gro", "Lillian", "Unni"]

m_slavic_gpt = ["Ivan", "Vladimir", "Sergei", "Alexander", "Dmitri", "Maxim", "Nikolai", "Andrei", "Viktor", "Pavel",
"Yuri", "Mikhail", "Boris", "Stanislav", "Oleg", "Evgeny", "Anton", "Konstantin", "Aleksandr", "Semyon"]

f_slavic_gpt = ["Anna", "Olga", "Maria", "Elena", "Natalia", "Tatiana", "Svetlana", "Irina", "Nadezhda", "Larisa",
"Yelena", "Lyubov", "Alla", "Veronika", "Irina", "Galina", "Ksenia", "Ekaterina", "Alina", "Anastasia"]


last_swe = ['Svensson', 'Andersson', 'Gustavsson', 'Gjertsson', 'Nilsson', 'Knutsson', 'Fredriksson', 'Lundgren', 'Fransson', 'Lundgren', 'Lindstedt', 'Mattsson', 'Ohlsson', 'Bengtsson', 'Lundberg', 'Lindberg', 'Ekstedt', 'Nordström']
last_gpt_eur0 =['Oliveira', 'Sandberg', 'Martin', 'Sousa', 'Garrido', 'Fonseca', 'Bjork', 'Gouveia', 'Pérez', 'Navarro', 'Silva', 'Pascual', 'Matos', 'Serrano', 'Ferreira', 'Jimenez', 'Lopez', 'Blanco', 'Romero', 'Edwards', 'Gonzalez', 'Santana', 'Coelho', 'Barros', 'Vieira', 'Larsson', 'Gomes', 'Castillo', 'Lundberg', 'Karlsson', 'Rodriguez', 'Berglund', 'Olsson', 'Cuesta', 'Diaz', 'Alonso', 'Andersson', 'Gomez', 'Bergstrom', 'Bengtsson', 'del Rio', 'Jonsson', 'Sanchez', 'Vazquez', 'Ribeiro', 'Jansson', 'Hidalgo', 'Castro', 'Petersson', 'Hansson', 'Carlsson', 'Vidal', 'Morales', 'Rivera', 'Santos', 'Faria', 'Gimenez', 'Sjogren', 'Perez', 'Andrade', 'Pacheco', 'Jakobsson', 'Berggren', 'Forsberg', 'Mendes', 'Ruiz', 'Jesus', 'Cardoso', 'Rodríguez', 'Eklund', 'Nunes', 'Ramalho', 'Persson', 'Eriksson', 'Gustafsson', 'Wallin', 'Soderberg', 'Molina', 'Garcia', 'Moreno', 'Alves', 'Rodrigues', 'Rocha', 'Barbosa', 'Alvarez', 'Martinez', 'Johansson', 'Svensson', 'Moura', 'Monteiro', 'Fernandez', 'Lopes', 'Pettersson', 'Suarez', 'Ortega', 'Costa', 'Pereira', 'Dominguez', 'Ramirez', 'Gómez', 'Teixeira', 'Ramos', 'Reyes', 'Lundqvist', 'Sundberg', 'Carvalho', 'Cabrera', 'Fernández', 'Martins', 'Torres', 'Pinto', 'Nilsson', 'Almeida', 'Lima', 'Neves', 'Hernandez', 'Vera', 'Marques']
last_gpt_eur1 = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"] # This doesn't seem very scandinavian
last_gpt_eur2 = ["Schmidt", "Schneider", "Fischer", "Müller", "Weber", "Schulz", "Wagner", "Becker", "Hoffmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", "Neumann", "Schwarz", "Braun", "Hofmann"] # This is also very weirdly distributed for a 'european name' prompt
last_gpt_asia = ["Kim", "Lee", "Park", "Wong", "Choi", "Li", "Zhang", "Lin", "Wu", "Chen", "Yuan", "Zhao", "Yang", "Huang", "Liu", "Guo", "Wang", "Sun", "Xu", "Gao"]
last_gpt_mena = ["Al-Saud", "Al-Shaikh", "Al-Maktoum", "Al-Sabah", "Al-Thani", "Bin Laden", "Al-Nasser", "Al-Hussein", "Al-Assad", "Al-Khalifa", "Al-Mahmoud", "Al-Hajri", "Al-Dhabi", "Al-Otaibi", "Al-Rumaihi", "Al-Ghanim", "Al-Mulla", "Al-Hariri", "Al-Mutairi", "Al-Sayed", "Hussein", "Mohammed", "Ahmed", "Ali", "Mahmoud", "Omar", "Abdullah", "Youssef", "Sayed", "Ibrahim", "Khan", "Hasan", "Qassem", "Rashid", "Tariq", "Jamal", "Faris", "Nashat", "Taleb", "Ghanem"]

# -------------------

# password_bucket
psw0 = ['sommar', 'qwerty', 'hejsan', 'stilet', 'password', 'mamma', 'volvo', 'sommar', 'hejhej', 'kungen', 'kalle', 'sverige', 'general', 'kalleanka', '123456',
 'password','12345678','qwerty','123456789','12345','1234','111111','1234567','dragon','123123','wrongpassword','abc123','football','monkey','letmein','696969','shadow','master','666666','qwertyuiop','123321','mustang','1234567890','michael','654321','pussy','superman','1qaz2wsx','7777777','abcdef','121212','000000','qazwsx','123qwe','killer','trustno1','jordan','jennifer','zxcvbnm','asdfgh','hunter','buster','soccer','harley','batman','andrew','tigger','sunshine','iloveyou','fuckme','2000','charlie','robert','thomas','hockey','ranger','daniel','starwars','klaster','112233','george','asshole','computer','michelle','jessica','pepper','easy','zxcvbn','555555','11111111','131313','freedom','777777','pass','fuck','maggie','159753','aaaaaa','ginger','princess','joshua','cheese','amanda','summer','love','ashley','6969','nicole','chelsea','biteme','matthew','access','yankees','987654321','dallas','austin','thunder','taylor','matrix','william','corvette','hello','martin','heather','secret','YourNan','merlin','diamond','1234qwer','gfhjkm','hammer','silver','222222','88888888','anthony','justin','test','bailey','q1w2e3r4t5','patrick','internet','scooter','orange','11111','golfer','cookie','richard','samantha','bigdog','guitar','jackson','whatever','mickey','chicken','sparky','snoopy','maverick','phoenix','camaro','sexy','peanut','morgan','welcome','falcon','cowboy','ferrari','samsung','andrea','smokey','steelers','joseph','mercedes','dakota','arsenal','eagles','melissa','boomer','booboo','spider','nascar','monster','tigers','yellow','xxxxxx','123123123','gateway','marina','diablo','bulldog','qwer1234','compaq','purple','hardcore','banana','junior','hannah','123654','porsche','lakers','iceman','money','cowboys','987654','london','tennis','999999','ncc1701','coffee','scooby','0000','miller','boston','q1w2e3r4','fuckoff','brandon','yamaha','chester','mother','forever','johnny','edward','333333','oliver','redsox','player','nikita','knight','fender','barney','midnight','please','brandy','chicago','badboy','iwantu','slayer','rangers','charles','angel','flower','bigdaddy','rabbit','wizard','bigdick','jasper','enter','rachel','chris','steven','winner','adidas','victoria','natasha','1q2w3e4r','jasmine','winter','prince','panties','marine','ghbdtn','fishing','cocacola','casper','james','232323','raiders','888888','marlboro','gandalf','asdfasdf','crystal','87654321','12344321','sexsex','golden','blowme','bigtits','8675309','panther','lauren','angela','bitch','spanky','thx1138','angels','madison','winston','shannon','mike','toyota','blowjob','jordan23','canada','sophie','Password','apples','dick','tiger','razz','123abc','pokemon','qazxsw','55555','qwaszx','muffin','johnson','murphy','cooper','jonathan','liverpoo','david','danielle','159357','jackie','1990','123456a','789456','turtle','horny','abcd1234','scorpion','qazwsxedc','101010','butter','carlos','password1','dennis','slipknot','qwerty123','booger','asdf','1991','black','startrek','12341234','cameron','newyork','rainbow','nathan','john','1992','rocket','viking','redskins','butthead','asdfghjkl','1212','sierra','peaches','gemini','doctor','wilson','sandra','helpme','qwertyui','victor','florida','dolphin','pookie','captain','tucker','blue','liverpool','theman','bandit','dolphins','maddog','packers','jaguar','lovers','nicholas','united','tiffany','maxwell','zzzzzz','nirvana','jeremy','suckit','stupid','porn','monica','elephant','giants','jackass','hotdog','rosebud','success','debbie','mountain','444444','xxxxxxxx','warrior','1q2w3e4r5t','q1w2e3','123456q','albert','metallic','lucky','azerty','7777','shithead','alex','bond007','alexis','1111111','samson','5150','willie','scorpio','bonnie','gators','benjamin','voodoo','driver','dexter','2112','jason','calvin','freddy','212121','creative','12345a','sydney','rush2112','1989','asdfghjk','red123','bubba','4815162342','passw0rd','trouble','gunner','happy','fucking','gordon','legend','jessie','stella','qwert','eminem','arthur','apple','nissan','bullshit','bear','america','1qazxsw2','nothing','parker','4444','rebecca','qweqwe','garfield','01012011','beavis','69696969','jack','asdasd','december','2222','102030','252525','11223344','magic','apollo','skippy','315475','girls','kitten','golf','copper','braves','shelby','godzilla','beaver','fred','tomcat','august','buddy','airborne','1993','1988','lifehack','qqqqqq','brooklyn','animal','platinum','phantom','online','xavier','darkness','blink182','power','fish','green','789456123','voyager','police','travis','12qwaszx','heaven','snowball','lover','abcdef','00000','pakistan','007007','walter','playboy','blazer','cricket','sniper','hooters','donkey','willow','loveme','saturn','therock','redwings','bigboy','pumpkin','trinity','williams','tits','nintendo','digital','destiny','topgun','runner','marvin','guinness','chance','bubbles','testing','fire','november','minecraft','asdf1234','lasvegas','sergey','broncos','cartman','private','celtic','birdie','little','cassie','babygirl','donald','beatles','1313','dickhead','family','12121212','school','louise','gabriel','eclipse','fluffy','147258369','lol123','explorer','beer','nelson','flyers','spencer','scott','lovely','gibson','doggie','cherry','andrey','snickers','buffalo','pantera','metallica','member','carter','qwertyu','peter','alexande','steve','bronco','paradise','goober','5555','samuel','montana','mexico','dreams','michigan','cock','carolina','yankee','friends','magnum','surfer','poopoo','maximus','genius','cool','vampire','lacrosse','asd123','aaaa','christin','kimberly','speedy','sharon','carmen','111222','kristina','sammy','racing','ou812','sabrina','horses','0987654321','qwerty1','pimpin','baby','stalker','enigma','147147','star','poohbear','boobies','147258','simple','bollocks','12345q','marcus','brian','1987','qweasdzxc','drowssap','hahaha','caroline','barbara','dave','viper','drummer','action','einstein','bitches','genesis','hello1','scotty','friend','forest','010203','hotrod','google','vanessa','spitfire','badger','maryjane','friday','alaska','1232323q','tester','jester','jake','champion','billy','147852','rock','hawaii','badass','chevy','420420','walker','stephen','eagle1','bill','1986','october','gregory','svetlana','pamela','1984','music','shorty','westside','stanley','diesel','courtney','242424','kevin','porno','hitman','boobs','mark','12345qwert','reddog','frank','qwe123','popcorn','patricia','aaaaaaaa','1969','teresa','mozart','buddha','anderson','paul','melanie','abcdefg','security','lucky1','lizard','denise','3333','a12345','123789','ruslan','stargate','simpsons','scarface','eagle','123456789a','thumper','olivia','naruto','1234554321','general','cherokee','a123456','vincent','Usuckballz1','spooky','qweasd','cumshot','free','frankie','douglas','death','1980','loveyou','kitty','kelly','veronica','suzuki','semperfi','penguin','mercury','liberty','spirit','scotland','natalie','marley','vikings','system','sucker','king','allison','marshall','1979','098765','qwerty12','hummer','adrian','1985','vfhbyf','sandman','rocky','leslie','antonio','98765432','4321','softball','passion','mnbvcxz','bastard','passport','horney','rascal','howard','franklin','bigred','assman','alexander','homer','redrum','jupiter','claudia','55555555','141414','zaq12wsx','shit','patches','nigger','cunt','raider','infinity','andre','54321','galore','college','russia','kawasaki','bishop','77777777','vladimir','money1','freeuser','wildcats','francis','disney','budlight','brittany','1994','00000000','sweet','oksana','honda','domino','bulldogs','brutus','swordfis','norman','monday','jimmy','ironman','ford','fantasy','9999','7654321','PASSWORD','hentai','duncan','cougar','1977','jeffrey','house','dancer','brooke','timothy','super','marines','justice','digger','connor','patriots','karina','202020','molly','everton','tinker','alicia','rasdzv3','poop','pearljam','stinky','naughty','colorado','123123a','water','test123','ncc1701d','motorola','ireland','asdfg','slut','matt','houston','boogie','zombie','accord','vision','bradley','reggie','kermit','froggy','ducati','avalon','6666','9379992','sarah','saints','logitech','chopper','852456','simpson','madonna','juventus','claire','159951','zachary','yfnfif','wolverin','warcraft','hello123','extreme','penis','peekaboo','fireman','eugene','brenda','123654789','russell','panthers','georgia','smith','skyline','jesus','elizabet','spiderma','smooth','pirate','empire','bullet','8888','virginia','valentin','psycho','predator','arizona','134679','mitchell','alyssa','vegeta','titanic','christ','goblue','fylhtq','wolf','mmmmmm','kirill','indian','hiphop','baxter','awesome','people','danger','roland','mookie','741852963','1111111111','dreamer','bambam','arnold','1981','skipper','serega','rolltide','elvis','changeme','simon','1q2w3e','lovelove','fktrcfylh','denver','tommy','mine','loverboy','hobbes','happy1','alison','nemesis','chevelle','cardinal','burton','wanker','picard','151515','tweety','michael1','147852369','12312','xxxx','windows','turkey','456789','1974','vfrcbv','sublime','1975','galina','bobby','newport','manutd','daddy','american','alexandr','1966','victory','rooster','qqq111','madmax','electric','bigcock','a1b2c3','wolfpack','spring','phpbb','lalala','suckme','spiderman','eric','darkside','classic','raptor','123456789q','hendrix','1982','wombat','avatar','alpha','zxc123','crazy','hard','england','brazil','1978','01011980','wildcat','polina','freepass']


# ------------------- #


if __name__ == "__main__":
    file_path = 'Data/name_corpus.pkl'

    lists_dict = {
        'm_sweden_gpt': m_sweden_gpt,
        'f_sweden_gpt': f_sweden_gpt,
        'f_norwa_list': f_norwa_list,
        'm_scandi_gpt': m_scandi_gpt,
        'f_scandi_gpt': f_scandi_gpt,
        'm_slavic_gpt': m_slavic_gpt,
        'f_slavic_gpt': f_slavic_gpt,
        'last_swe': last_swe,
        'last_gpt_eur0': last_gpt_eur0,
        'last_gpt_eur2': last_gpt_eur2,
        'last_gpt_asia': last_gpt_asia,
        'last_gpt_mena': last_gpt_mena
    }

    with open(file_path, 'wb') as file:
        pickle.dump(lists_dict, file)

    print(f"Saved as {file_path}")