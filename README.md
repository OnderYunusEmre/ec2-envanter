\# EC2 Envanter Aracı



boto3 ile AWS hesabındaki EC2 instance'larını listeleyip CSV'ye yazan bir Python aracı.



\## Gereksinimler



\- Python 3.10+

\- AWS CLI

\- Bir IAM kullanıcısı (yalnızca EC2 okuma yetkisiyle)



\## Kurulum



```powershell

py -m pip install boto3

aws configure

```



`aws configure` adımında erişim anahtarı, gizli anahtar ve bölge bilgisini girersin. Anahtarlar koda ya da repoya yazılmaz.



\## Kullanım



```powershell

py src\\ec2\_envanter.py --bolge eu-central-1 --cikti envanter.csv

```



| Parametre | Açıklama | Varsayılan |

|-----------|----------|------------|

| `--bolge` | AWS bölgesi | `eu-central-1` |

| `--cikti` | Çıktı CSV dosyası | `envanter.csv` |



\## Örnek Çıktı



Terminal:



```

1 instance bulundu, 'envanter.csv' dosyasına yazıldı.

```



CSV:



```csv

instance\_id,tip,durum,bolge

i-0123456789abcdef0,t3.micro,running,eu-central-1

```



\## Güvenlik



Erişim anahtarları kodda tutulmaz. `.gitignore` CSV ve kimlik dosyalarını repo dışında bırakır.

