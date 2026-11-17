import argparse
import csv

import boto3
from botocore.exceptions import ClientError, EndpointConnectionError, NoCredentialsError, ProfileNotFound


def ec2_instance_listele(bolge):
    ec2 = boto3.client("ec2", region_name=bolge)
    satirlar = []
    for sayfa in ec2.get_paginator("describe_instances").paginate():
        for rezervasyon in sayfa["Reservations"]:
            for instance in rezervasyon["Instances"]:
                satirlar.append({
                    "instance_id": instance["InstanceId"],
                    "tip": instance["InstanceType"],
                    "durum": instance["State"]["Name"],
                    "bolge": bolge,
                })
    return satirlar


def csv_yaz(satirlar, dosya_adi):
    with open(dosya_adi, "w", newline="", encoding="utf-8") as f:
        yazici = csv.DictWriter(f, fieldnames=["instance_id", "tip", "durum", "bolge"])
        yazici.writeheader()
        yazici.writerows(satirlar)


def main():
    parser = argparse.ArgumentParser(description="EC2 instance envanteri çıkarır.")
    parser.add_argument("--bolge", default="eu-central-1", help="AWS bölgesi")
    parser.add_argument("--cikti", default="envanter.csv", help="CSV dosya adı")
    args = parser.parse_args()

    try:
        satirlar = ec2_instance_listele(args.bolge)
    except ProfileNotFound as e:
        print(f"Hata: AWS profili bulunamadı: {e}")
        return
    except NoCredentialsError:
        print("Hata: AWS kimlik bilgisi bulunamadı. 'aws configure' ile yapılandırın.")
        return
    except EndpointConnectionError:
        print(f"Hata: '{args.bolge}' bölgesine bağlanılamadı. Bölge adını kontrol edin.")
        return
    except ClientError as e:
        kod = e.response["Error"]["Code"]
        if kod in ("UnauthorizedOperation", "AccessDenied", "AuthFailure"):
            print("Hata: Bu kullanıcının EC2 okuma yetkisi yok. IAM politikasını kontrol edin.")
        else:
            print(f"AWS hatası: {kod} - {e}")
        return

    csv_yaz(satirlar, args.cikti)
    print(f"{len(satirlar)} instance bulundu, '{args.cikti}' dosyasına yazıldı.")


if __name__ == "__main__":
    main()