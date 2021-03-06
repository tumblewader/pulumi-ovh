// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface CloudNetworkPrivateRegionsStatus {
    region: string;
    /**
     * the status of the network. should be normally set to 'ACTIVE'.
     */
    status: string;
}

export interface CloudNetworkPrivateSubnetIpPool {
    /**
     * Enable DHCP.
     * Changing this forces a new resource to be created. Defaults to false.
     * _
     */
    dhcp: boolean;
    /**
     * Last ip for this region.
     * Changing this value recreates the subnet.
     */
    end: string;
    /**
     * Global network in CIDR format.
     * Changing this value recreates the subnet
     */
    network: string;
    /**
     * The region in which the network subnet will be created.
     * Ex.: "GRA1". Changing this value recreates the resource.
     */
    region: string;
    /**
     * First ip for this region.
     * Changing this value recreates the subnet.
     */
    start: string;
}

export interface CloudUserRole {
    /**
     * A description associated with the user.
     */
    description: string;
    /**
     * id of the role
     */
    id: string;
    /**
     * name of the role
     */
    name: string;
    /**
     * list of permissions associated with the role
     */
    permissions: string[];
}

export interface DedicatedServerInstallTaskDetails {
    /**
     * Template change log details.
     */
    changeLog?: string;
    /**
     * Set up the server using the provided hostname instead of the default hostname.
     */
    customHostname?: string;
    /**
     * Disk group id.
     */
    diskGroupId?: number;
    /**
     * set to true to install RTM.
     */
    installRtm?: boolean;
    /**
     * set to true to install sql server (Windows template only).
     */
    installSqlServer?: boolean;
    /**
     * language.
     */
    language?: string;
    /**
     * set to true to disable RAID.
     */
    noRaid?: boolean;
    /**
     * Indicate the URL where your postinstall customisation script is located.
     */
    postInstallationScriptLink?: string;
    /**
     * Indicate the string returned by your postinstall customisation script on successful execution. Advice: your script should return a unique validation string in case of succes. A good example is 'loh1Xee7eo OK OK OK UGh8Ang1Gu'.
     */
    postInstallationScriptReturn?: string;
    /**
     * set to true to make a hardware raid reset.
     */
    resetHwRaid?: boolean;
    /**
     * soft raid devices.
     */
    softRaidDevices?: number;
    /**
     * Name of the ssh key that should be installed. Password login will be disabled.
     */
    sshKeyName?: string;
    /**
     * Use the distribution's native kernel instead of the recommended OVH Kernel.
     */
    useDistribKernel?: boolean;
    /**
     * set to true to use SPLA.
     */
    useSpla?: boolean;
}

export interface GetCloudRegionService {
    /**
     * The name of the region associated with the public cloud
     * project.
     */
    name: string;
    /**
     * the status of the service
     */
    status: string;
}

export interface GetDedicatedServerVni {
    /**
     * VirtualNetworkInterface activation state
     */
    enabled: boolean;
    /**
     * VirtualNetworkInterface mode (public,vrack,vrack_aggregation)
     */
    mode: string;
    /**
     * User defined VirtualNetworkInterface name
     */
    name: string;
    nics: string[];
    /**
     * Server bound to this VirtualNetworkInterface
     */
    serverName: string;
    /**
     * VirtualNetworkInterface unique id
     */
    uuid: string;
    /**
     * vRack name
     */
    vrack: string;
}

export interface GetIPLoadbalancingOrderableZone {
    /**
     * The zone three letter code
     */
    name: string;
    /**
     * The billing planCode for this zone
     */
    planCode: string;
}

export interface GetMeInstallationTemplateCustomization {
    changeLog: string;
    customHostname: string;
    postInstallationScriptLink: string;
    postInstallationScriptReturn: string;
    rating: number;
    sshKeyName: string;
    useDistributionKernel: boolean;
}

export interface GetMeInstallationTemplatePartitionScheme {
    hardwareRaids: outputs.GetMeInstallationTemplatePartitionSchemeHardwareRaid[];
    name: string;
    partitions: outputs.GetMeInstallationTemplatePartitionSchemePartition[];
    priority: number;
}

export interface GetMeInstallationTemplatePartitionSchemeHardwareRaid {
    disks: string[];
    mode: string;
    name: string;
    step: number;
}

export interface GetMeInstallationTemplatePartitionSchemePartition {
    filesystem: string;
    mountpoint: string;
    order: number;
    raid: string;
    size: number;
    type: string;
    volumeName: string;
}

export interface GetPublicCloudRegionService {
    /**
     * the name of the public cloud service
     */
    name: string;
    /**
     * the status of the service
     */
    status: string;
}

export interface GetVPSDatacenter {
    longname: string;
    name: string;
}

export interface GetVPSModel {
    name: string;
    offer: string;
    version: string;
}

export interface IPLoadbalancingHTTPFarmProbe {
    /**
     * Force use of SSL (TLS)
     */
    forceSsl?: boolean;
    /**
     * probe interval, Value between 30 and 3600 seconds, default 30
     */
    interval?: number;
    /**
     * What to mach `pattern` against (`contains`, `default`, `internal`, `matches`, `status`)
     */
    match: string;
    /**
     * HTTP probe method (`GET`, `HEAD`, `OPTIONS`, `internal`)
     */
    method: string;
    /**
     * Negate probe result
     */
    negate?: boolean;
    /**
     * Pattern to match against `match`
     */
    pattern: string;
    /**
     * Port for backends to recieve traffic on.
     */
    port: number;
    /**
     * Valid values : `http`, `internal`, `mysql`, `oko`, `pgsql`, `smtp`, `tcp`
     */
    type: string;
    /**
     * URL for HTTP probe type.
     */
    url: string;
}

export interface IPLoadbalancingHTTPRouteAction {
    status?: number;
    target?: string;
    type: string;
}

export interface IPLoadbalancingTCPFarmProbe {
    /**
     * Force use of SSL (TLS)
     */
    forceSsl?: boolean;
    /**
     * probe interval, Value between 30 and 3600 seconds, default 30
     */
    interval?: number;
    /**
     * What to mach `pattern` against (`contains`, `default`, `internal`, `matches`, `status`)
     */
    match?: string;
    /**
     * HTTP probe method (`GET`, `HEAD`, `OPTIONS`, `internal`)
     */
    method?: string;
    /**
     * Negate probe result
     */
    negate?: boolean;
    /**
     * Pattern to match against `match`
     */
    pattern?: string;
    /**
     * Port for backends to recieve traffic on.
     */
    port?: number;
    /**
     * Valid values : `http`, `internal`, `mysql`, `oko`, `pgsql`, `smtp`, `tcp`
     */
    type: string;
    /**
     * URL for HTTP probe type.
     */
    url?: string;
}

export interface MeInstallationTemplateCustomization {
    changeLog?: string;
    customHostname?: string;
    postInstallationScriptLink?: string;
    postInstallationScriptReturn?: string;
    rating?: number;
    sshKeyName?: string;
    useDistributionKernel?: boolean;
}

export interface PubicCloudPrivateNetworkRegionsStatus {
    region: string;
    /**
     * the status of the network. should be normally set to 'ACTIVE'.
     */
    status: string;
}

export interface PubicCloudPrivateNetworkSubnetIpPool {
    /**
     * Enable DHCP.
     * Changing this forces a new resource to be created. Defaults to false.
     * _
     */
    dhcp: boolean;
    /**
     * Last ip for this region.
     * Changing this value recreates the subnet.
     */
    end: string;
    /**
     * Global network in CIDR format.
     * Changing this value recreates the subnet
     */
    network: string;
    /**
     * The region in which the network subnet will be created.
     * Ex.: "GRA1". Changing this value recreates the resource.
     */
    region: string;
    /**
     * First ip for this region.
     * Changing this value recreates the subnet.
     */
    start: string;
}

export interface PublicCloudUserRole {
    /**
     * A description associated with the user.
     */
    description: string;
    id: string;
    name: string;
    permissions: string[];
}

