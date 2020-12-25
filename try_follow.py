from selenium import webdriver
import ntplib
import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

user = ['ady_prasojo', 'puspitajeng', 'rumah_muslim145', 'nnisamalia', 'arinahygea', 'arinpe', 'dimasfw28', 'evaardelia', 'ftriahas', 'ginasitepu', 'constellatia', 'helgaproborini', 'ichtiya', 'iganuryanti', 'inggitbp', 'kartikapa', 'laks_abimanyu', 'faruqyismid', 'prabowo.39', 'muhammadirdal', 'nadiarezkyeliza', 'natasyaps', 'nidarhmh', 'nilaphrgt', 'nurinamf', 'regijaw', 'riaoktavv', 'salmautamima', 'septidiany', 'sofianurfadilla', 'sylviasuparno', 'tiaranadya', 'tiffanyvalensss', 'vidiarti', 'widihs', 'yara.cantika', 'yvtwdt', 'zeryy_ariyanda', 'yogaalfajri', 'yeniulvia', 'yasiirfadillah', 'yantiyunita3', 'nandafauza22', 'tarywulandary', 'yonaanjarasmara', 'tyakbarr', 'syarifahulieyazuhra', 'siscaanggrainii', 'sindyamwddh', 'sariiseptiiani', 'saabiraaa', 'rosi_idaa', 'adriansahrizky', 'rizkysyawal97', 'rahmatprabowo93', 'putrikarlinazulfikar', 'pdarmayani', 'nyakdarajunimarza', 'khairanuswatull', 'nurilahanta', 'nandasukma__', 'muuzammil', 'mysrptra_', 'mucelis', 'ariel_tae', 'zakiimuhammad', 'dr._yusuf_mhd', 'muhammadsyahrilghufran', 'muhammadrizky47', 'mirzanr', 'merryyunanda', 'maysaraahhh', 'ican_kly', 'intanfarhani96', 'ikram_kaoy', 'heenaanasha', 'jibbrril', 'fitriandini2', 'ferizainisyahna3', 'fty_azr', 'destayuorlandaa', 'cutmfraa', 'cutdeby', 'cutannisarj', 'deffi.nc', 'ayuanndaa', 'arsito_012', 'annisyahzulmi_', 'amaliahamini', 'alfazripp', 'akmalulhadi_', 'adli_96', 'adel_adelianz', 'aldilotalima', 'mhmilhaaam', 'dipineo', 'shintiaaritha', 'anaasiyya', 'ikapvrnama', 'ferayunita95', 'alexkgan', 'egiatika', 'ghaliamayuna', 'akiltasrif', 'dearamadana', 'rafajarsrg', 'lisarahmaasril', 'gitanajmi', 'salfianark', 'dumsarh', 'athirahartini', 'tmerdekap', 'yonifaa', 'wikusoma', 'telavaniumri', 'framitaainur', 'iswanramdhana', 'rezadelvita', 'aisyahsoit', 'ashilaputri', 'docnil_88', 'adebetris', 'harissetiadr', 'yandaarf', 'uswatundesky', 'dhilasyahrul', 'loplamblangong', 'nrlmsfrh', 'imanmastura', 'ellyanggiashinta', 'magdalenalbs', 'alif_fw', 'natasyputrii', 'oolrizky', 'syarifah_kiki', 'camelii4', 'tiararoza', 'bebbybalqis', 'faranitameutia', 'sevrinaya94', 'malabenjamin', 'keenandnanda', 'indahagungaprilia', 'hijdrianm', 'tiaranandaputri', 'mharisrmdhn', 'rahmatasmi16', 'trieshadinda', 'putrahsb4', 'maisyabila', 'oktaviawidyasari', 'mrrizkiramadhan', 'tiaayumarini', 'kusumahutapea', 'citanopriani', 'riniarbiee', 'putrirahmadhani.md', 'ferinamegasilvia96', 'fuadizain', 'novoniaa', 'yhaanggraini', 'dotspls_', 'suci_k_marthadia', 'wndsmla', 'dianrozani', 'karinatantri', 'rabinams', 'zhafirasz', 'ghinaa_ahmad', 'ndnisa', 'nadiatulaidila', 'sagitapp', 'apriliaaryyuhana', 'vellagysha', 'yoanawidi', 'retnaayuw', 'thariqahmad14', 'auliaajeng', 'lisangigihprakoso', 'nendesmita', 'wirawanab', 'maharani151195', 'miftahultsani', 'triasihamalya1', 'reyhansyahra', 'evajannati', 'agalbima', 'ugiksugianti', 'wisnuharyonugroho', 'dwiyuliaw', 'damarjatikp', 'anaraws_', 'guggytryan', 'nadyagitau', 'mdpinoko', 'titikmeilasari', 'galang19pradana', 'deangam', 'vianaprilya', 'dwiaguskur', 'hanifahdekainsani', 'bem.fkunmul', 'ratutrianandya', 'jokomaromon', 'dwikurniadian', 'ansarasit', 'grasiance', 'mina_qyo', 'ozzyyunandar', 'yusufbhas', 'renyindriyani', 'valentimoy', 'bem.fkunmul', 'jumadil_akbarriansyah', 'annaftryna', 'fahroniiarifin', 'mahlinan', 'debbyanggtams', 'ahlina.hanifah', 'fahreza_wardhana', 'claudia.purnama', 'arisindrawan', 'eldacitra', 'ikhlasulamalabdal', 'amalianrzzh', 'afanurul720', 'listaa_s', 'eriaeria22', 'adelfinahana', 'aphar_odhe', 'tenriuleng', 'alilf_22', 'nuraidahrizkya', 'renhaa_rsy', 'heylia___', 'sriramadanias', 'agriawanalhikmah', 'abrahamisnann', 'riri.sofyan', 'ahmadabqar', 'alunkhairunnisa', 'amaliagrahani', 'amiruzachra', 'abprayogo', 'anisjulianti', 'ansastri', 'sitt.a', 'ayeziayes', 'azibagusms', 'bobzirazvidi', 'didingkusuma', 'galuhgantina', 'dinyul', 'dwiipwt', 'xkmrd_', 'erahasanudin', 'farabillaha', 'dilarmdhani', 'febygethia', 'fernitacahya', 'ferzafarizky', 'anindyahfitri', 'ghanimd', 'ghinaanzani', 'ghinahanifahk', 'putrihh', 'hasanahsuci', 'hera.hera.here', 'irmalitahrdt', 'jihaanea', 'josiwanda', 'khildazakiyyahsaadah', 'kdanendrap', 'santangnuroh', 'masithohnurr', 'mentarinurfarida264', 'irsyadmhmd', 'faiq_akmal', 'muhammadfahmi_', 'muhammadharly', 'mandaniml', 'sigitharyan', 'mulkymau', 'nabilaaac', 'nabilahrh', 'nadyaaayuph', 'nadyamuja', 'nafishajaidii', 'angierivern', 'riansrmdhn', 'nindahsarii', 'ainii_nurul', 'ravenawarman', 'refidanimunawar', 'riztiriri', 'sakelakel', 'aldinahazard', 'sumiosahara', 'tiaraaandarini', 'tiffanyrchm', 'urwatulwtsq', 'vanyayesha', 'vergatorada', 'wijdanisharfina', 'wfahmulya', 'idhanbaiti', 'tri_meiningsih', 'anggitasetiadi', 'yulitaswandani', 'adamsujoko', 'dialaras', 'desitriutami', 'miaomp', 'nadyahasnar', 'nadashauti', 'mochrizkif', 'sitsarrah', 'intan.savitri', 'faizinsanul', 'fikrybaron', 'sidiqmhmmd19', 'rismaorchita10', 'sekarkinasihsp', 'hnkalita', 'intan_ulla', 'ratihmega', 'k.bregas', 'lorisnahardiknas', 'tzdarajat', 'anisadindan', 'rannisayuni13', 'belljov', 'fatiaaa9', 'faldicksaputra']
user = list(dict.fromkeys(user))[300:]
print(len(user))

username = 'autofind.isip@gmail.com'
password = 'Bakuganshoot123'

# setting webdriver
chrome_options = Options()  
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.instagram.com')
print('instagram opened')

element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
                                           
input_username = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
input_username.send_keys(username)
input_password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
input_password.send_keys(password)
input_password.send_keys(Keys.RETURN)
print('logging in')
time.sleep(5)

for i in range(len(user)):
    print()
    print(str(i).rjust(3) + ' ' + user[i].ljust(20), end=' ')
    browser.get('https://www.instagram.com/' + user[i])
    time.sleep(60)
    try:
        element = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
                (By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button')))
        print('requested', end=' ')
        element.click()
        continue
    except:
        pass

    try:
        element = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
                (By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')))
        print('followed', end=' ')
        element.click()
        continue
    except:
        print('button not found', end=' ')
        pass

    
