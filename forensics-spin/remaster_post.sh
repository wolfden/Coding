#!/bin/sh
PKGS_DIR="/sabayon/remaster/pkgs"
CHROOT_PKGS_DIR="${CHROOT_DIR}/var/lib/entropy/client/packages"
echo "Merging back packages"
cp "${CHROOT_PKGS_DIR}"/* "${PKGS_DIR}"/ -Ra
rm -rf "${CHROOT_PKGS_DIR}"{,-nonfree,-restricted}/*
cp -rv /home/gru/Git/Coding/forensics-spin/files/usr "${CHROOT_DIR}/"
cp -rv /home/gru/Git/Coding/forensics-spin/files/etc "${CHROOT_DIR}/"
sudo glib-compile-schemas "${CHROOT_DIR}/usr/share/glib-2.0/schemas/"
gsettings set org.gnome.shell.extensions.dash-to-dock extended-height true
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position LEFT
gsettings set org.gnome.shell.extensions.dash-to-dock transparency-mode DYNAMIC
gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 32
gsettings set org.gnome.shell.extensions.dash-to-dock custom-theme-shrink true

is_64=$(file "${CHROOT_DIR}"/bin/bash | grep "x86-64")
if [ -n "${is_64}" ]; then
    echo "equo cleanup" | chroot "${CHROOT_DIR}"
else
    echo "equo cleanup" | linux32 chroot "${CHROOT_DIR}"
fi
