%bcond_without check
%global debug_package %{nil}

%global crate getrandom

Name:           rust-%{crate}
Version:        0.2.15
Release:        1
Summary:        Small cross-platform library for retrieving random data from system source

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/getrandom
Source:         %{crates_source}
# Initial patched metadata
# * No non-unix deps
Patch0:         getrandom-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Small cross-platform library for retrieving random data from system source.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compiler_builtins-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compiler_builtins-devel %{_description}

This package contains library source intended for building other packages
which use "compiler_builtins" feature of "%{crate}" crate.

%files       -n %{name}+compiler_builtins-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages
which use "core" feature of "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-dep-of-std-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-dep-of-std" feature of "%{crate}" crate.

%files       -n %{name}+rustc-dep-of-std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
