Name:    lsd
Version: 1
Release: 1%{?dist}
Summary: Say hello, Texas style

License: MIT
Source0: lsd
BuildArch: noarch

%description
lsd... Yes..

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/lsd

%changelog