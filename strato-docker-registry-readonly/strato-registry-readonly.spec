Name:           strato-registry-readonly
Version:        1.0
Release:        1%{?dist}
License:        Stratoscale
Summary:        Stratoscale Registry Files

%description
Files needed for strato's docker registry readonly service.

%build
cp $TOP/strato-docker-registry-readonly/docker-registry-readonly.service .
cp $TOP/strato-docker-registry-readonly/docker-registry-readonly.yml .
cp $TOP/strato-docker-registry-readonly/docker-registry-readonly.service.clustermanager .

%install
install -d %{buildroot}/etc/stratoscale/compose/rootfs-star/
install -pm 644 docker-registry-readonly.yml %{buildroot}/etc/stratoscale/compose/rootfs-star/
install -d %{buildroot}/usr/lib/systemd/system
install -pm 644 docker-registry-readonly.service %{buildroot}/usr/lib/systemd/system/
install -d %{buildroot}/etc/stratoscale/clustermanager/services/control/
install -pm 644 docker-registry-readonly.service.clustermanager %{buildroot}/etc/stratoscale/clustermanager/services/control/docker-registry-readonly.service

%files
/usr/lib/systemd/system/docker-registry-readonly.service
/etc/stratoscale/compose/rootfs-star/docker-registry-readonly.yml
/etc/stratoscale/clustermanager/services/control/docker-registry-readonly.service
