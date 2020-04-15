%global _bindir /usr/local/bin

Name: docker-runc
Version: 1.0.0.rc3
Release: 104
Summary: runc is a CLI tool for spawning and running containers according to the OCI specification.

License: ASL 2.0
Source: %{name}.tar.gz

URL: https://www.opencontainers.org/
Vendor: OCI
Packager: OCI

BuildRequires: golang >= 1.8.3 glibc-static make libseccomp-devel libseccomp-static libselinux-devel

%description
runc is a CLI tool for spawning and running containers according to the OCI specification.

%prep
%setup -c -n runc

%install
./apply-patch 

mkdir -p .gopath/src/github.com/opencontainers
export GOPATH=`pwd`/.gopath
ln -sf `pwd` .gopath/src/github.com/opencontainers/runc
cd .gopath/src/github.com/opencontainers/runc
make BUILDTAGS="seccomp selinux" static 
rm -rf .gopath

install -d $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 runc $RPM_BUILD_ROOT/%{_bindir}/runc

%clean
%{__rm} -rf %{_bindir}/runc

%files
%{_bindir}/runc

%changelog
