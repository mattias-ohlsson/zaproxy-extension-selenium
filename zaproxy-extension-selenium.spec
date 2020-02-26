%global extension_id selenium
%global extension_name Selenium
%global extension_info WebDriver provider and includes HtmlUnit browser.
%global extension_infoUrl /docs/desktop/addons/selenium/
%global addon_folder %{extension_id}

Name:           zaproxy-extension-%{extension_id}
Version:        15.1.0
Release:        1%{?dist}
Summary:        %{extension_name} extension

License:        ASL 2.0
URL:            https://www.zaproxy.org%{extension_infoUrl}
Source0:        https://github.com/zaproxy/zap-extensions/archive/%{extension_id}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-11-openjdk-headless
Requires:       zaproxy

%description
%{extension_info}

%prep
%autosetup -n zap-extensions-%{extension_id}-v%{version}

%build
JAVA_HOME=/usr/lib/jvm/jre-11-openjdk ./gradlew :addOns:$(echo %{addon_folder} | tr / :):build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_datadir}/zaproxy/plugin
install -m 644 addOns/%{addon_folder}/build/zapAddOn/bin/*-%{version}.zap \
 %{buildroot}%{_datadir}/zaproxy/plugin

%files
%license LICENSE
%doc README.md CONTRIBUTING.md addOns/%{addon_folder}/CHANGELOG.md
%{_datadir}/zaproxy/plugin/*-%{version}.zap

%changelog
* Wed Feb 26 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 15.1.0-1
- Initial build
