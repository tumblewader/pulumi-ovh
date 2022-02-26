// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// > __DEPRECATED:__ Use `CloudNetworkPrivateSubnet` instead.
//
// Creates a subnet in a private network of a public cloud project.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-ovh/sdk/go/ovh"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ovh.NewPubicCloudPrivateNetworkSubnet(ctx, "subnet", &ovh.PubicCloudPrivateNetworkSubnetArgs{
// 			Dhcp:      pulumi.Bool(true),
// 			End:       pulumi.String("192.168.168.200"),
// 			Network:   pulumi.String("192.168.168.0/24"),
// 			NetworkId: pulumi.String("0234543"),
// 			NoGateway: pulumi.Bool(false),
// 			ProjectId: pulumi.String("67890"),
// 			Region:    pulumi.String("GRA1"),
// 			Start:     pulumi.String("192.168.168.100"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type PubicCloudPrivateNetworkSubnet struct {
	pulumi.CustomResourceState

	// Ip Block representing the subnet cidr.
	Cidr pulumi.StringOutput `pulumi:"cidr"`
	// Enable DHCP.
	// Changing this forces a new resource to be created. Defaults to false.
	// _
	Dhcp pulumi.BoolPtrOutput `pulumi:"dhcp"`
	// Last ip for this region.
	// Changing this value recreates the subnet.
	End pulumi.StringOutput `pulumi:"end"`
	// The IP of the gateway
	GatewayIp pulumi.StringOutput `pulumi:"gatewayIp"`
	// List of ip pools allocated in the subnet.
	// * `ip_pools/network` - Global network with cidr.
	// * `ip_pools/region` - Region where this subnet is created.
	// * `ip_pools/dhcp` - DHCP enabled.
	// * `ip_pools/end` - Last ip for this region.
	// * `ip_pools/start` - First ip for this region.
	IpPools PubicCloudPrivateNetworkSubnetIpPoolArrayOutput `pulumi:"ipPools"`
	// Global network in CIDR format.
	// Changing this value recreates the subnet
	Network pulumi.StringOutput `pulumi:"network"`
	// The id of the network.
	// Changing this forces a new resource to be created.
	NetworkId pulumi.StringOutput `pulumi:"networkId"`
	// Set to true if you don't want to set a default gateway IP.
	// Changing this value recreates the resource. Defaults to false.
	NoGateway pulumi.BoolPtrOutput `pulumi:"noGateway"`
	// The id of the public cloud project. If omitted,
	// the `OVH_PROJECT_ID` environment variable is used.
	// Changing this forces a new resource to be created.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The region in which the network subnet will be created.
	// Ex.: "GRA1". Changing this value recreates the resource.
	Region pulumi.StringOutput `pulumi:"region"`
	// First ip for this region.
	// Changing this value recreates the subnet.
	Start pulumi.StringOutput `pulumi:"start"`
}

// NewPubicCloudPrivateNetworkSubnet registers a new resource with the given unique name, arguments, and options.
func NewPubicCloudPrivateNetworkSubnet(ctx *pulumi.Context,
	name string, args *PubicCloudPrivateNetworkSubnetArgs, opts ...pulumi.ResourceOption) (*PubicCloudPrivateNetworkSubnet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.End == nil {
		return nil, errors.New("invalid value for required argument 'End'")
	}
	if args.Network == nil {
		return nil, errors.New("invalid value for required argument 'Network'")
	}
	if args.NetworkId == nil {
		return nil, errors.New("invalid value for required argument 'NetworkId'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	if args.Region == nil {
		return nil, errors.New("invalid value for required argument 'Region'")
	}
	if args.Start == nil {
		return nil, errors.New("invalid value for required argument 'Start'")
	}
	var resource PubicCloudPrivateNetworkSubnet
	err := ctx.RegisterResource("ovh:index/pubicCloudPrivateNetworkSubnet:PubicCloudPrivateNetworkSubnet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPubicCloudPrivateNetworkSubnet gets an existing PubicCloudPrivateNetworkSubnet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPubicCloudPrivateNetworkSubnet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PubicCloudPrivateNetworkSubnetState, opts ...pulumi.ResourceOption) (*PubicCloudPrivateNetworkSubnet, error) {
	var resource PubicCloudPrivateNetworkSubnet
	err := ctx.ReadResource("ovh:index/pubicCloudPrivateNetworkSubnet:PubicCloudPrivateNetworkSubnet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PubicCloudPrivateNetworkSubnet resources.
type pubicCloudPrivateNetworkSubnetState struct {
	// Ip Block representing the subnet cidr.
	Cidr *string `pulumi:"cidr"`
	// Enable DHCP.
	// Changing this forces a new resource to be created. Defaults to false.
	// _
	Dhcp *bool `pulumi:"dhcp"`
	// Last ip for this region.
	// Changing this value recreates the subnet.
	End *string `pulumi:"end"`
	// The IP of the gateway
	GatewayIp *string `pulumi:"gatewayIp"`
	// List of ip pools allocated in the subnet.
	// * `ip_pools/network` - Global network with cidr.
	// * `ip_pools/region` - Region where this subnet is created.
	// * `ip_pools/dhcp` - DHCP enabled.
	// * `ip_pools/end` - Last ip for this region.
	// * `ip_pools/start` - First ip for this region.
	IpPools []PubicCloudPrivateNetworkSubnetIpPool `pulumi:"ipPools"`
	// Global network in CIDR format.
	// Changing this value recreates the subnet
	Network *string `pulumi:"network"`
	// The id of the network.
	// Changing this forces a new resource to be created.
	NetworkId *string `pulumi:"networkId"`
	// Set to true if you don't want to set a default gateway IP.
	// Changing this value recreates the resource. Defaults to false.
	NoGateway *bool `pulumi:"noGateway"`
	// The id of the public cloud project. If omitted,
	// the `OVH_PROJECT_ID` environment variable is used.
	// Changing this forces a new resource to be created.
	ProjectId *string `pulumi:"projectId"`
	// The region in which the network subnet will be created.
	// Ex.: "GRA1". Changing this value recreates the resource.
	Region *string `pulumi:"region"`
	// First ip for this region.
	// Changing this value recreates the subnet.
	Start *string `pulumi:"start"`
}

type PubicCloudPrivateNetworkSubnetState struct {
	// Ip Block representing the subnet cidr.
	Cidr pulumi.StringPtrInput
	// Enable DHCP.
	// Changing this forces a new resource to be created. Defaults to false.
	// _
	Dhcp pulumi.BoolPtrInput
	// Last ip for this region.
	// Changing this value recreates the subnet.
	End pulumi.StringPtrInput
	// The IP of the gateway
	GatewayIp pulumi.StringPtrInput
	// List of ip pools allocated in the subnet.
	// * `ip_pools/network` - Global network with cidr.
	// * `ip_pools/region` - Region where this subnet is created.
	// * `ip_pools/dhcp` - DHCP enabled.
	// * `ip_pools/end` - Last ip for this region.
	// * `ip_pools/start` - First ip for this region.
	IpPools PubicCloudPrivateNetworkSubnetIpPoolArrayInput
	// Global network in CIDR format.
	// Changing this value recreates the subnet
	Network pulumi.StringPtrInput
	// The id of the network.
	// Changing this forces a new resource to be created.
	NetworkId pulumi.StringPtrInput
	// Set to true if you don't want to set a default gateway IP.
	// Changing this value recreates the resource. Defaults to false.
	NoGateway pulumi.BoolPtrInput
	// The id of the public cloud project. If omitted,
	// the `OVH_PROJECT_ID` environment variable is used.
	// Changing this forces a new resource to be created.
	ProjectId pulumi.StringPtrInput
	// The region in which the network subnet will be created.
	// Ex.: "GRA1". Changing this value recreates the resource.
	Region pulumi.StringPtrInput
	// First ip for this region.
	// Changing this value recreates the subnet.
	Start pulumi.StringPtrInput
}

func (PubicCloudPrivateNetworkSubnetState) ElementType() reflect.Type {
	return reflect.TypeOf((*pubicCloudPrivateNetworkSubnetState)(nil)).Elem()
}

type pubicCloudPrivateNetworkSubnetArgs struct {
	// Enable DHCP.
	// Changing this forces a new resource to be created. Defaults to false.
	// _
	Dhcp *bool `pulumi:"dhcp"`
	// Last ip for this region.
	// Changing this value recreates the subnet.
	End string `pulumi:"end"`
	// Global network in CIDR format.
	// Changing this value recreates the subnet
	Network string `pulumi:"network"`
	// The id of the network.
	// Changing this forces a new resource to be created.
	NetworkId string `pulumi:"networkId"`
	// Set to true if you don't want to set a default gateway IP.
	// Changing this value recreates the resource. Defaults to false.
	NoGateway *bool `pulumi:"noGateway"`
	// The id of the public cloud project. If omitted,
	// the `OVH_PROJECT_ID` environment variable is used.
	// Changing this forces a new resource to be created.
	ProjectId string `pulumi:"projectId"`
	// The region in which the network subnet will be created.
	// Ex.: "GRA1". Changing this value recreates the resource.
	Region string `pulumi:"region"`
	// First ip for this region.
	// Changing this value recreates the subnet.
	Start string `pulumi:"start"`
}

// The set of arguments for constructing a PubicCloudPrivateNetworkSubnet resource.
type PubicCloudPrivateNetworkSubnetArgs struct {
	// Enable DHCP.
	// Changing this forces a new resource to be created. Defaults to false.
	// _
	Dhcp pulumi.BoolPtrInput
	// Last ip for this region.
	// Changing this value recreates the subnet.
	End pulumi.StringInput
	// Global network in CIDR format.
	// Changing this value recreates the subnet
	Network pulumi.StringInput
	// The id of the network.
	// Changing this forces a new resource to be created.
	NetworkId pulumi.StringInput
	// Set to true if you don't want to set a default gateway IP.
	// Changing this value recreates the resource. Defaults to false.
	NoGateway pulumi.BoolPtrInput
	// The id of the public cloud project. If omitted,
	// the `OVH_PROJECT_ID` environment variable is used.
	// Changing this forces a new resource to be created.
	ProjectId pulumi.StringInput
	// The region in which the network subnet will be created.
	// Ex.: "GRA1". Changing this value recreates the resource.
	Region pulumi.StringInput
	// First ip for this region.
	// Changing this value recreates the subnet.
	Start pulumi.StringInput
}

func (PubicCloudPrivateNetworkSubnetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pubicCloudPrivateNetworkSubnetArgs)(nil)).Elem()
}

type PubicCloudPrivateNetworkSubnetInput interface {
	pulumi.Input

	ToPubicCloudPrivateNetworkSubnetOutput() PubicCloudPrivateNetworkSubnetOutput
	ToPubicCloudPrivateNetworkSubnetOutputWithContext(ctx context.Context) PubicCloudPrivateNetworkSubnetOutput
}

func (*PubicCloudPrivateNetworkSubnet) ElementType() reflect.Type {
	return reflect.TypeOf((**PubicCloudPrivateNetworkSubnet)(nil)).Elem()
}

func (i *PubicCloudPrivateNetworkSubnet) ToPubicCloudPrivateNetworkSubnetOutput() PubicCloudPrivateNetworkSubnetOutput {
	return i.ToPubicCloudPrivateNetworkSubnetOutputWithContext(context.Background())
}

func (i *PubicCloudPrivateNetworkSubnet) ToPubicCloudPrivateNetworkSubnetOutputWithContext(ctx context.Context) PubicCloudPrivateNetworkSubnetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PubicCloudPrivateNetworkSubnetOutput)
}

// PubicCloudPrivateNetworkSubnetArrayInput is an input type that accepts PubicCloudPrivateNetworkSubnetArray and PubicCloudPrivateNetworkSubnetArrayOutput values.
// You can construct a concrete instance of `PubicCloudPrivateNetworkSubnetArrayInput` via:
//
//          PubicCloudPrivateNetworkSubnetArray{ PubicCloudPrivateNetworkSubnetArgs{...} }
type PubicCloudPrivateNetworkSubnetArrayInput interface {
	pulumi.Input

	ToPubicCloudPrivateNetworkSubnetArrayOutput() PubicCloudPrivateNetworkSubnetArrayOutput
	ToPubicCloudPrivateNetworkSubnetArrayOutputWithContext(context.Context) PubicCloudPrivateNetworkSubnetArrayOutput
}

type PubicCloudPrivateNetworkSubnetArray []PubicCloudPrivateNetworkSubnetInput

func (PubicCloudPrivateNetworkSubnetArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PubicCloudPrivateNetworkSubnet)(nil)).Elem()
}

func (i PubicCloudPrivateNetworkSubnetArray) ToPubicCloudPrivateNetworkSubnetArrayOutput() PubicCloudPrivateNetworkSubnetArrayOutput {
	return i.ToPubicCloudPrivateNetworkSubnetArrayOutputWithContext(context.Background())
}

func (i PubicCloudPrivateNetworkSubnetArray) ToPubicCloudPrivateNetworkSubnetArrayOutputWithContext(ctx context.Context) PubicCloudPrivateNetworkSubnetArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PubicCloudPrivateNetworkSubnetArrayOutput)
}

// PubicCloudPrivateNetworkSubnetMapInput is an input type that accepts PubicCloudPrivateNetworkSubnetMap and PubicCloudPrivateNetworkSubnetMapOutput values.
// You can construct a concrete instance of `PubicCloudPrivateNetworkSubnetMapInput` via:
//
//          PubicCloudPrivateNetworkSubnetMap{ "key": PubicCloudPrivateNetworkSubnetArgs{...} }
type PubicCloudPrivateNetworkSubnetMapInput interface {
	pulumi.Input

	ToPubicCloudPrivateNetworkSubnetMapOutput() PubicCloudPrivateNetworkSubnetMapOutput
	ToPubicCloudPrivateNetworkSubnetMapOutputWithContext(context.Context) PubicCloudPrivateNetworkSubnetMapOutput
}

type PubicCloudPrivateNetworkSubnetMap map[string]PubicCloudPrivateNetworkSubnetInput

func (PubicCloudPrivateNetworkSubnetMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PubicCloudPrivateNetworkSubnet)(nil)).Elem()
}

func (i PubicCloudPrivateNetworkSubnetMap) ToPubicCloudPrivateNetworkSubnetMapOutput() PubicCloudPrivateNetworkSubnetMapOutput {
	return i.ToPubicCloudPrivateNetworkSubnetMapOutputWithContext(context.Background())
}

func (i PubicCloudPrivateNetworkSubnetMap) ToPubicCloudPrivateNetworkSubnetMapOutputWithContext(ctx context.Context) PubicCloudPrivateNetworkSubnetMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PubicCloudPrivateNetworkSubnetMapOutput)
}

type PubicCloudPrivateNetworkSubnetOutput struct{ *pulumi.OutputState }

func (PubicCloudPrivateNetworkSubnetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PubicCloudPrivateNetworkSubnet)(nil)).Elem()
}

func (o PubicCloudPrivateNetworkSubnetOutput) ToPubicCloudPrivateNetworkSubnetOutput() PubicCloudPrivateNetworkSubnetOutput {
	return o
}

func (o PubicCloudPrivateNetworkSubnetOutput) ToPubicCloudPrivateNetworkSubnetOutputWithContext(ctx context.Context) PubicCloudPrivateNetworkSubnetOutput {
	return o
}

type PubicCloudPrivateNetworkSubnetArrayOutput struct{ *pulumi.OutputState }

func (PubicCloudPrivateNetworkSubnetArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PubicCloudPrivateNetworkSubnet)(nil)).Elem()
}

func (o PubicCloudPrivateNetworkSubnetArrayOutput) ToPubicCloudPrivateNetworkSubnetArrayOutput() PubicCloudPrivateNetworkSubnetArrayOutput {
	return o
}

func (o PubicCloudPrivateNetworkSubnetArrayOutput) ToPubicCloudPrivateNetworkSubnetArrayOutputWithContext(ctx context.Context) PubicCloudPrivateNetworkSubnetArrayOutput {
	return o
}

func (o PubicCloudPrivateNetworkSubnetArrayOutput) Index(i pulumi.IntInput) PubicCloudPrivateNetworkSubnetOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PubicCloudPrivateNetworkSubnet {
		return vs[0].([]*PubicCloudPrivateNetworkSubnet)[vs[1].(int)]
	}).(PubicCloudPrivateNetworkSubnetOutput)
}

type PubicCloudPrivateNetworkSubnetMapOutput struct{ *pulumi.OutputState }

func (PubicCloudPrivateNetworkSubnetMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PubicCloudPrivateNetworkSubnet)(nil)).Elem()
}

func (o PubicCloudPrivateNetworkSubnetMapOutput) ToPubicCloudPrivateNetworkSubnetMapOutput() PubicCloudPrivateNetworkSubnetMapOutput {
	return o
}

func (o PubicCloudPrivateNetworkSubnetMapOutput) ToPubicCloudPrivateNetworkSubnetMapOutputWithContext(ctx context.Context) PubicCloudPrivateNetworkSubnetMapOutput {
	return o
}

func (o PubicCloudPrivateNetworkSubnetMapOutput) MapIndex(k pulumi.StringInput) PubicCloudPrivateNetworkSubnetOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PubicCloudPrivateNetworkSubnet {
		return vs[0].(map[string]*PubicCloudPrivateNetworkSubnet)[vs[1].(string)]
	}).(PubicCloudPrivateNetworkSubnetOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PubicCloudPrivateNetworkSubnetInput)(nil)).Elem(), &PubicCloudPrivateNetworkSubnet{})
	pulumi.RegisterInputType(reflect.TypeOf((*PubicCloudPrivateNetworkSubnetArrayInput)(nil)).Elem(), PubicCloudPrivateNetworkSubnetArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PubicCloudPrivateNetworkSubnetMapInput)(nil)).Elem(), PubicCloudPrivateNetworkSubnetMap{})
	pulumi.RegisterOutputType(PubicCloudPrivateNetworkSubnetOutput{})
	pulumi.RegisterOutputType(PubicCloudPrivateNetworkSubnetArrayOutput{})
	pulumi.RegisterOutputType(PubicCloudPrivateNetworkSubnetMapOutput{})
}