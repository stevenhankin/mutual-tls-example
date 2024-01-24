To generate a test key and certificate (crt) file for testing purposes, you can use OpenSSL, a widely-used open-source toolkit for working with SSL/TLS protocols. Below are the steps to generate a self-signed certificate along with a private key:

### Step 1: Install OpenSSL

Make sure you have OpenSSL installed on your system. You can download OpenSSL from the official website or install it using a package manager relevant to your operating system.

### Step 2: Generate a Private Key

Open a terminal or command prompt and run the following command to generate a private key:

```bash
openssl genpkey -algorithm RSA -out key.pem
```

This command generates an RSA private key and saves it to a file named `key.pem`.

### Step 3: Generate a Certificate Signing Request (CSR)

Next, create a Certificate Signing Request (CSR) with the following command:

```bash
openssl req -new -key key.pem -out csr.pem
```

You will be prompted to enter information such as the Common Name (CN), organization, and others. The Common Name is typically the domain name for which you are creating the certificate. For testing purposes, you can use something like "localhost" as the Common Name.

### Step 4: Generate a Self-Signed Certificate

Now, use the CSR to generate a self-signed certificate:

```bash
openssl x509 -req -in csr.pem -signkey key.pem -out cert.pem
```

This command generates a self-signed certificate (`cert.pem`) using the private key (`key.pem`) and the CSR (`csr.pem`).

### Step 5: Verify the Certificate

You can verify the contents of the certificate using the following command:

```bash
openssl x509 -text -noout -in cert.pem
```

This will display detailed information about the certificate.

Now, you have a test key (`key.pem`) and a self-signed certificate (`cert.pem`) that you can use for testing purposes. Keep in mind that for production use, you should obtain certificates from a trusted Certificate Authority (CA).

```bash

for app in client server
do
  openssl genpkey -algorithm RSA -out ${app}-key.pem
  openssl req -new -key ${app}-key.pem -out ${app}-csr.pem
  openssl x509 -req -in ${app}-csr.pem -signkey ${app}-key.pem -out ${app}-cert.pem
done



```
