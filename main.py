import ssl

# test python interpreter. If it outputs LibreSSL, then you are using wrong (system) python.
print(ssl.OPENSSL_VERSION)