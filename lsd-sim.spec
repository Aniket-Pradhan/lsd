Name:    lsd-sim
Version: 1.1.0
Release: 1%{?dist}
Summary: A Cheap psychedelic simulator

License: MIT
Source0: lsd-sim
BuildArch: noarch

%description
lsd... Yes please.

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/lsd-sim

%changelog
* Sat Aug 24 2019 Aniket Pradhan <aniket17133@iiitd.ac.in> - 1.1.0 - 1
- v1.1.0 release.