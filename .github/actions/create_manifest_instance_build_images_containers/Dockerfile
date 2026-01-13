FROM docker.io/library/python:3.13@sha256:4f3780acb8d126492a8890a1e1715d36773c0cc1865b5aa569ba857548d0f51f AS builder

COPY images_containers_manifest.py /images_containers_manifest.py

ENTRYPOINT /images_containers_manifest.py
