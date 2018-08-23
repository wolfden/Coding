#!/bin/bash
rm -rf /usr/share/backgrounds/iottinka
glib-compile-schemas /usr/share/glib-2.0/schemas
emaint --fix world
