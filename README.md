# K6 Test Loader

A load and performance testing project using k6 with Kubernetes for testing APIs and web applications.

## Prerequisites

- [Kubernetes](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download) installed
- Git

## Installation

```bash
git clone <your-repo>
cd k6-test-loader
```

## Usage

```bash
source ./scripts/run-loader.sh <version> <result_output_folder>
```

* make sure Kubernets is up and running
* make sure to configure script in the config file
* make sure to create the right result output folder

## Project Structure

```
├── README.md
├── scripts/          # K6 test scripts
├── config/           # Kubernetes configuration files
└── results/          # Generated reports
```

## Contributing

Please follow these guidelines to contribute to this project:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

MIT