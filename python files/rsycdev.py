#!/bin/bash
 
# Set some vars
MIRROR_URL="ftp.SURFnet.nl"
 
 
echo -e "\nWelcome to the Sabayon Linux(tm) Syncmaster scripty!"
echo -e "These are your options, choose wisely!\n"
echo "[1] Sabayon_Linux_DAILY_amd64_KDE"
echo "[2] Sabayon_Linux_DAILY_amd64_KDE-dev"
echo "[3] Sabayon_Linux_DAILY_amd64_GNOME"
echo "[4] Sabayon_Linux_DAILY_amd64_GNOME-dev"
echo "[5] Sabayon_Linux_DAILY_amd64_MATE"
echo "[6] Sabayon_Linux_DAILY_amd64_MATE-dev"
echo "[7] Sabayon_Linux_DAILY_amd64_Xfce"
echo "[8] Sabayon_Linux_DAILY_amd64_Xfce-dev"
echo -e "\n"
echo "Please tell me what you need: "
read version_to_get
 
case $version_to_get in
    1)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_KDE"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_KDE.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_KDE.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_KDE.iso.pkglist .
        ;;
    2)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_KDE-dev"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_KDE-dev.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_KDE-dev.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_KDE-dev.iso.pkglist .
        ;;
    3)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_GNOME"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_GNOME.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_GNOME.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_GNOME.iso.pkglist .
        ;;
    4)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_GNOME-dev"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_GNOME-dev.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_GNOME-dev.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_GNOME-dev.iso.pkglist .
        ;;
    5)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_MATE"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_MATE.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_MATE.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_MATE.iso.pkglist .
        ;;
    6)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_MATE-dev"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_MATE-dev.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_MATE-dev.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_MATE-dev.iso.pkglist .
        ;;
    7)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_Xfce"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_Xfce.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_Xfce.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_Xfce.iso.pkglist .
        ;;
    8)
                echo "Here we go!"
                sleep 1
        echo "Getting Sabayon_Linux_DAILY_amd64_Xfce-dev"
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_Xfce-dev.iso .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_Xfce-dev.iso.md5 .
                rsync -av rsync://$MIRROR_URL/sabayonlinux/iso/daily/Sabayon_Linux_DAILY_amd64_Xfce-dev.iso.pkglist .
        ;;
    *)
        echo "Invalid choice, you suck."
esac