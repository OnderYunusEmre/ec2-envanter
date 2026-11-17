# EC2 Envanter Aracı

boto3 ile AWS hesabındaki EC2 instance'larını listeleyip CSV'ye yazan bir Python aracı.

## Gereksinimler

- Python 3.10 veya üstü
- AWS CLI
- Yalnızca EC2 okuma yetkisi olan bir IAM kullanıcısı

## Kurulum

py -m pip install boto3
aws configure

`aws configure` adımında erişim anahtarı, gizli anahtar ve bölge bilgisini girersin. Bu bilgiler koda ya da repoya yazılmaz.

## Kullanım

py src\ec2_envanter.py --bolge eu-central-1 --cikti envanter.csv

| Parametre | Açıklama | Varsayılan |
|-----------|----------|------------|
| `--bolge` | AWS bölgesi | `eu-central-1` |
| `--cikti` | Çıktı CSV dosyası | `envanter.csv` |

## Hata Yönetimi

- Profil bulunamazsa anlaşılır bir mesaj verir.
- Kimlik bilgisi yoksa `aws configure` çalıştırılmasını önerir.
- Geçersiz bölgede bağlantı hatası mesajı gösterir.
- EC2 okuma yetkisi yoksa IAM politikasını kontrol etmeyi önerir.

## Güvenlik

Erişim anahtarları kodda tutulmaz. `.gitignore` CSV ve kimlik dosyalarını repo dışında bırakır.
