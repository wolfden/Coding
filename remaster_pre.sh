#!/bin/sh
PKGS_DIR="/sabayon/remaster/pkgs"
CHROOT_PKGS_DIR="${CHROOT_DIR}/var/lib/entropy/client/packages"
[[ ! -d "${PKGS_DIR}" ]] && mkdir -p "${PKGS_DIR}"
[[ ! -d "${CHROOT_PKGS_DIR}" ]] && mkdir -p "${CHROOT_PKGS_DIR}"
echo "Mounting packages over"
rm -rf "${CHROOT_PKGS_DIR}"/*
cp ${PKGS_DIR}/* "${CHROOT_PKGS_DIR}"/ -Ra
exit 0
