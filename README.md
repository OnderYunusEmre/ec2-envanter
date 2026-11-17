# EC2 Inventory Tool

A small Python tool that lists the EC2 instances in your AWS account and writes their details to a CSV file. It uses **boto3**, the AWS SDK for Python.

## Features

- Lists all EC2 instances in a chosen AWS region
- Exports instance ID, type, state, and region to a CSV file
- Region and output file are configurable from the command line
- Clear error messages for missing profiles, missing credentials, invalid regions, and missing permissions
- No credentials stored in the code

## Requirements

- Python 3.10 or newer
- AWS CLI
- An IAM user with read-only EC2 permissions (`AmazonEC2ReadOnlyAccess`)

## Installation

1. Install the boto3 library:

```
py -m pip install boto3
```

2. Configure your AWS credentials:

```
aws configure
```

You will be asked for:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name (for example, `eu-central-1`)
- Default output format (`json`)

The credentials are saved in your local AWS configuration folder, not in this project.

3. Check that the connection works:

```
aws sts get-caller-identity
```

The output should show the ARN of the IAM user you configured.

## Usage

Run the tool from the project folder:

```
py src\ec2_envanter.py --bolge eu-central-1 --cikti envanter.csv
```

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--bolge` | AWS region to scan | `eu-central-1` |
| `--cikti` | Output CSV file name | `envanter.csv` |

Example to scan another region and write to a different file:

```
py src\ec2_envanter.py --bolge eu-west-1 --cikti irlanda.csv
```

## Example Output

Console:

```
1 instance bulundu, 'envanter.csv' dosyasına yazıldı.
```

CSV file (`envanter.csv`):

```
instance_id,tip,durum,bolge
i-0123456789abcdef0,t3.micro,running,eu-central-1
```

## Output Columns

| Column | Meaning |
|--------|---------|
| `instance_id` | Unique ID of the EC2 instance |
| `tip` | Instance type (size and hardware) |
| `durum` | Current state, such as `running` or `stopped` |
| `bolge` | AWS region where the instance is located |

## Error Handling

| Situation | Message |
|-----------|---------|
| AWS profile not found | Tells you the profile does not exist |
| No credentials configured | Suggests running `aws configure` |
| Invalid or unreachable region | Asks you to check the region name |
| Missing EC2 read permission | Suggests checking the IAM policy |
| Other AWS errors | Shows the AWS error code and message |

## Security

- Access keys are never written in the code or committed to Git.
- `.gitignore` excludes `.env`, CSV files, `credentials`, and `*.pem` files.
- The tool only reads data. It does not start, stop, or delete any resource.
- The IAM user has read-only permissions, following the principle of least privilege.

## Project Structure

```
ec2-envanter/
├── README.md
├── .gitignore
└── src/
    └── ec2_envanter.py
```

## Cost Note

Listing EC2 instances does not create resources, so it does not add cost. Running instances, however, are billed by AWS, so the inventory is useful for spotting resources that should be stopped.

---

# EC2 Envanter Aracı (Türkçe)

Bu küçük Python aracı, AWS hesabınızdaki EC2 sunucularını listeler ve bilgilerini bir CSV dosyasına yazar. **boto3** kütüphanesini (Python için AWS SDK) kullanır.

## Özellikler

- Seçilen AWS bölgesindeki tüm EC2 sunucularını listeler
- Sunucu ID'sini, tipini, durumunu ve bölgesini CSV dosyasına yazar
- Bölge ve çıktı dosyası komut satırından ayarlanabilir
- Profil yoksa, kimlik bilgisi eksikse, bölge geçersizse ya da yetki yoksa anlaşılır hata mesajları verir
- Kodda hiçbir kimlik bilgisi saklanmaz

## Gereksinimler

- Python 3.10 veya üstü
- AWS CLI
- Yalnızca EC2 okuma yetkisi olan bir IAM kullanıcısı (`AmazonEC2ReadOnlyAccess`)

## Kurulum

1. boto3 kütüphanesini kurun:

```
py -m pip install boto3
```

2. AWS kimlik bilgilerinizi yapılandırın:

```
aws configure
```

Sizden şunlar istenir:
- AWS Access Key ID
- AWS Secret Access Key
- Varsayılan bölge (örneğin `eu-central-1`)
- Varsayılan çıktı formatı (`json`)

Bu bilgiler proje klasörüne değil, bilgisayarınızdaki AWS yapılandırma klasörüne kaydedilir.

3. Bağlantıyı test edin:

```
aws sts get-caller-identity
```

Çıktıda yapılandırdığınız IAM kullanıcısının ARN'i görünmelidir.

## Kullanım

Aracı proje klasöründen çalıştırın:

```
py src\ec2_envanter.py --bolge eu-central-1 --cikti envanter.csv
```

### Parametreler

| Parametre | Açıklama | Varsayılan |
|-----------|----------|------------|
| `--bolge` | Taranacak AWS bölgesi | `eu-central-1` |
| `--cikti` | Çıktı CSV dosyasının adı | `envanter.csv` |

Başka bir bölgeyi farklı bir dosyaya yazmak için:

```
py src\ec2_envanter.py --bolge eu-west-1 --cikti irlanda.csv
```

## Örnek Çıktı

Terminal:

```
1 instance bulundu, 'envanter.csv' dosyasına yazıldı.
```

CSV dosyası (`envanter.csv`):

```
instance_id,tip,durum,bolge
i-0123456789abcdef0,t3.micro,running,eu-central-1
```

## Çıktı Sütunları

| Sütun | Anlamı |
|-------|--------|
| `instance_id` | EC2 sunucusunun benzersiz kimliği |
| `tip` | Sunucu tipi (boyut ve donanım) |
| `durum` | Mevcut durumu, örneğin `running` veya `stopped` |
| `bolge` | Sunucunun bulunduğu AWS bölgesi |

## Hata Yönetimi

| Durum | Mesaj |
|-------|-------|
| AWS profili bulunamadı | Profilin mevcut olmadığını belirtir |
| Kimlik bilgisi yapılandırılmamış | `aws configure` çalıştırmayı önerir |
| Bölge geçersiz ya da erişilemiyor | Bölge adını kontrol etmeyi önerir |
| EC2 okuma yetkisi yok | IAM politikasını kontrol etmeyi önerir |
| Diğer AWS hataları | AWS hata kodunu ve mesajını gösterir |

## Güvenlik

- Erişim anahtarları koda yazılmaz ve Git'e eklenmez.
- `.gitignore`, `.env` dosyalarını, CSV dosyalarını, `credentials` dosyasını ve `*.pem` dosyalarını dışarıda tutar.
- Araç yalnızca okuma yapar. Hiçbir kaynağı başlatmaz, durdurmaz ya da silmez.
- IAM kullanıcısı yalnızca okuma yetkisine sahiptir (en az yetki prensibi).

## Proje Yapısı

```
ec2-envanter/
├── README.md
├── .gitignore
└── src/
    └── ec2_envanter.py
```

## Maliyet Notu

EC2 sunucularını listelemek yeni kaynak oluşturmaz, dolayısıyla ek maliyet çıkarmaz. Ancak çalışan sunucular AWS tarafından ücretlendirilir, bu yüzden envanter, gereksiz yere açık kalan sunucuları bulmak için kullanışlıdır.