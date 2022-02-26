// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a backend http server group (frontend) to be used by loadbalancing frontend(s)
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
// 		lb, err := ovh.GetIPLoadbalancing(ctx, &GetIPLoadbalancingArgs{
// 			ServiceName: pulumi.StringRef("ip-1.2.3.4"),
// 			State:       pulumi.StringRef("ok"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		farm80, err := ovh.NewIPLoadbalancingHTTPFarm(ctx, "farm80", &ovh.IPLoadbalancingHTTPFarmArgs{
// 			DisplayName: pulumi.String("ingress-8080-gra"),
// 			Port:        pulumi.Int(80),
// 			ServiceName: pulumi.String(lb.ServiceName),
// 			Zone:        pulumi.String("all"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ovh.NewIPLoadbalancingHTTPFrontend(ctx, "testfrontend", &ovh.IPLoadbalancingHTTPFrontendArgs{
// 			DefaultFarmId: farm80.ID(),
// 			DisplayName:   pulumi.String("ingress-8080-gra"),
// 			Port:          pulumi.String("80,443"),
// 			ServiceName:   pulumi.String(lb.ServiceName),
// 			Zone:          pulumi.String("all"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type IPLoadbalancingHTTPFrontend struct {
	pulumi.CustomResourceState

	// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
	AllowedSources pulumi.StringArrayOutput `pulumi:"allowedSources"`
	// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
	DedicatedIpfos pulumi.StringArrayOutput `pulumi:"dedicatedIpfos"`
	// Default TCP Farm of your frontend
	DefaultFarmId pulumi.IntOutput `pulumi:"defaultFarmId"`
	// Default ssl served to your customer
	DefaultSslId pulumi.IntOutput `pulumi:"defaultSslId"`
	// Disable your frontend. Default: 'false'
	Disabled pulumi.BoolPtrOutput `pulumi:"disabled"`
	// Human readable name for your frontend, this field is for you
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// Port(s) attached to your frontend. Supports single port (numerical value),
	// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
	// and/or 'range'. Each port must be in the [1;49151] range
	Port pulumi.StringOutput `pulumi:"port"`
	// The internal name of your IP load balancing
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// SSL deciphering. Default: 'false'
	Ssl pulumi.BoolPtrOutput `pulumi:"ssl"`
	// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewIPLoadbalancingHTTPFrontend registers a new resource with the given unique name, arguments, and options.
func NewIPLoadbalancingHTTPFrontend(ctx *pulumi.Context,
	name string, args *IPLoadbalancingHTTPFrontendArgs, opts ...pulumi.ResourceOption) (*IPLoadbalancingHTTPFrontend, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Port == nil {
		return nil, errors.New("invalid value for required argument 'Port'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	if args.Zone == nil {
		return nil, errors.New("invalid value for required argument 'Zone'")
	}
	var resource IPLoadbalancingHTTPFrontend
	err := ctx.RegisterResource("ovh:index/iPLoadbalancingHTTPFrontend:IPLoadbalancingHTTPFrontend", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIPLoadbalancingHTTPFrontend gets an existing IPLoadbalancingHTTPFrontend resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIPLoadbalancingHTTPFrontend(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IPLoadbalancingHTTPFrontendState, opts ...pulumi.ResourceOption) (*IPLoadbalancingHTTPFrontend, error) {
	var resource IPLoadbalancingHTTPFrontend
	err := ctx.ReadResource("ovh:index/iPLoadbalancingHTTPFrontend:IPLoadbalancingHTTPFrontend", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IPLoadbalancingHTTPFrontend resources.
type iploadbalancingHTTPFrontendState struct {
	// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
	AllowedSources []string `pulumi:"allowedSources"`
	// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
	DedicatedIpfos []string `pulumi:"dedicatedIpfos"`
	// Default TCP Farm of your frontend
	DefaultFarmId *int `pulumi:"defaultFarmId"`
	// Default ssl served to your customer
	DefaultSslId *int `pulumi:"defaultSslId"`
	// Disable your frontend. Default: 'false'
	Disabled *bool `pulumi:"disabled"`
	// Human readable name for your frontend, this field is for you
	DisplayName *string `pulumi:"displayName"`
	// Port(s) attached to your frontend. Supports single port (numerical value),
	// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
	// and/or 'range'. Each port must be in the [1;49151] range
	Port *string `pulumi:"port"`
	// The internal name of your IP load balancing
	ServiceName *string `pulumi:"serviceName"`
	// SSL deciphering. Default: 'false'
	Ssl *bool `pulumi:"ssl"`
	// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
	Zone *string `pulumi:"zone"`
}

type IPLoadbalancingHTTPFrontendState struct {
	// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
	AllowedSources pulumi.StringArrayInput
	// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
	DedicatedIpfos pulumi.StringArrayInput
	// Default TCP Farm of your frontend
	DefaultFarmId pulumi.IntPtrInput
	// Default ssl served to your customer
	DefaultSslId pulumi.IntPtrInput
	// Disable your frontend. Default: 'false'
	Disabled pulumi.BoolPtrInput
	// Human readable name for your frontend, this field is for you
	DisplayName pulumi.StringPtrInput
	// Port(s) attached to your frontend. Supports single port (numerical value),
	// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
	// and/or 'range'. Each port must be in the [1;49151] range
	Port pulumi.StringPtrInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringPtrInput
	// SSL deciphering. Default: 'false'
	Ssl pulumi.BoolPtrInput
	// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
	Zone pulumi.StringPtrInput
}

func (IPLoadbalancingHTTPFrontendState) ElementType() reflect.Type {
	return reflect.TypeOf((*iploadbalancingHTTPFrontendState)(nil)).Elem()
}

type iploadbalancingHTTPFrontendArgs struct {
	// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
	AllowedSources []string `pulumi:"allowedSources"`
	// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
	DedicatedIpfos []string `pulumi:"dedicatedIpfos"`
	// Default TCP Farm of your frontend
	DefaultFarmId *int `pulumi:"defaultFarmId"`
	// Default ssl served to your customer
	DefaultSslId *int `pulumi:"defaultSslId"`
	// Disable your frontend. Default: 'false'
	Disabled *bool `pulumi:"disabled"`
	// Human readable name for your frontend, this field is for you
	DisplayName *string `pulumi:"displayName"`
	// Port(s) attached to your frontend. Supports single port (numerical value),
	// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
	// and/or 'range'. Each port must be in the [1;49151] range
	Port string `pulumi:"port"`
	// The internal name of your IP load balancing
	ServiceName string `pulumi:"serviceName"`
	// SSL deciphering. Default: 'false'
	Ssl *bool `pulumi:"ssl"`
	// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
	Zone string `pulumi:"zone"`
}

// The set of arguments for constructing a IPLoadbalancingHTTPFrontend resource.
type IPLoadbalancingHTTPFrontendArgs struct {
	// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
	AllowedSources pulumi.StringArrayInput
	// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
	DedicatedIpfos pulumi.StringArrayInput
	// Default TCP Farm of your frontend
	DefaultFarmId pulumi.IntPtrInput
	// Default ssl served to your customer
	DefaultSslId pulumi.IntPtrInput
	// Disable your frontend. Default: 'false'
	Disabled pulumi.BoolPtrInput
	// Human readable name for your frontend, this field is for you
	DisplayName pulumi.StringPtrInput
	// Port(s) attached to your frontend. Supports single port (numerical value),
	// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
	// and/or 'range'. Each port must be in the [1;49151] range
	Port pulumi.StringInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringInput
	// SSL deciphering. Default: 'false'
	Ssl pulumi.BoolPtrInput
	// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
	Zone pulumi.StringInput
}

func (IPLoadbalancingHTTPFrontendArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*iploadbalancingHTTPFrontendArgs)(nil)).Elem()
}

type IPLoadbalancingHTTPFrontendInput interface {
	pulumi.Input

	ToIPLoadbalancingHTTPFrontendOutput() IPLoadbalancingHTTPFrontendOutput
	ToIPLoadbalancingHTTPFrontendOutputWithContext(ctx context.Context) IPLoadbalancingHTTPFrontendOutput
}

func (*IPLoadbalancingHTTPFrontend) ElementType() reflect.Type {
	return reflect.TypeOf((**IPLoadbalancingHTTPFrontend)(nil)).Elem()
}

func (i *IPLoadbalancingHTTPFrontend) ToIPLoadbalancingHTTPFrontendOutput() IPLoadbalancingHTTPFrontendOutput {
	return i.ToIPLoadbalancingHTTPFrontendOutputWithContext(context.Background())
}

func (i *IPLoadbalancingHTTPFrontend) ToIPLoadbalancingHTTPFrontendOutputWithContext(ctx context.Context) IPLoadbalancingHTTPFrontendOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPLoadbalancingHTTPFrontendOutput)
}

// IPLoadbalancingHTTPFrontendArrayInput is an input type that accepts IPLoadbalancingHTTPFrontendArray and IPLoadbalancingHTTPFrontendArrayOutput values.
// You can construct a concrete instance of `IPLoadbalancingHTTPFrontendArrayInput` via:
//
//          IPLoadbalancingHTTPFrontendArray{ IPLoadbalancingHTTPFrontendArgs{...} }
type IPLoadbalancingHTTPFrontendArrayInput interface {
	pulumi.Input

	ToIPLoadbalancingHTTPFrontendArrayOutput() IPLoadbalancingHTTPFrontendArrayOutput
	ToIPLoadbalancingHTTPFrontendArrayOutputWithContext(context.Context) IPLoadbalancingHTTPFrontendArrayOutput
}

type IPLoadbalancingHTTPFrontendArray []IPLoadbalancingHTTPFrontendInput

func (IPLoadbalancingHTTPFrontendArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPLoadbalancingHTTPFrontend)(nil)).Elem()
}

func (i IPLoadbalancingHTTPFrontendArray) ToIPLoadbalancingHTTPFrontendArrayOutput() IPLoadbalancingHTTPFrontendArrayOutput {
	return i.ToIPLoadbalancingHTTPFrontendArrayOutputWithContext(context.Background())
}

func (i IPLoadbalancingHTTPFrontendArray) ToIPLoadbalancingHTTPFrontendArrayOutputWithContext(ctx context.Context) IPLoadbalancingHTTPFrontendArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPLoadbalancingHTTPFrontendArrayOutput)
}

// IPLoadbalancingHTTPFrontendMapInput is an input type that accepts IPLoadbalancingHTTPFrontendMap and IPLoadbalancingHTTPFrontendMapOutput values.
// You can construct a concrete instance of `IPLoadbalancingHTTPFrontendMapInput` via:
//
//          IPLoadbalancingHTTPFrontendMap{ "key": IPLoadbalancingHTTPFrontendArgs{...} }
type IPLoadbalancingHTTPFrontendMapInput interface {
	pulumi.Input

	ToIPLoadbalancingHTTPFrontendMapOutput() IPLoadbalancingHTTPFrontendMapOutput
	ToIPLoadbalancingHTTPFrontendMapOutputWithContext(context.Context) IPLoadbalancingHTTPFrontendMapOutput
}

type IPLoadbalancingHTTPFrontendMap map[string]IPLoadbalancingHTTPFrontendInput

func (IPLoadbalancingHTTPFrontendMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPLoadbalancingHTTPFrontend)(nil)).Elem()
}

func (i IPLoadbalancingHTTPFrontendMap) ToIPLoadbalancingHTTPFrontendMapOutput() IPLoadbalancingHTTPFrontendMapOutput {
	return i.ToIPLoadbalancingHTTPFrontendMapOutputWithContext(context.Background())
}

func (i IPLoadbalancingHTTPFrontendMap) ToIPLoadbalancingHTTPFrontendMapOutputWithContext(ctx context.Context) IPLoadbalancingHTTPFrontendMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPLoadbalancingHTTPFrontendMapOutput)
}

type IPLoadbalancingHTTPFrontendOutput struct{ *pulumi.OutputState }

func (IPLoadbalancingHTTPFrontendOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IPLoadbalancingHTTPFrontend)(nil)).Elem()
}

func (o IPLoadbalancingHTTPFrontendOutput) ToIPLoadbalancingHTTPFrontendOutput() IPLoadbalancingHTTPFrontendOutput {
	return o
}

func (o IPLoadbalancingHTTPFrontendOutput) ToIPLoadbalancingHTTPFrontendOutputWithContext(ctx context.Context) IPLoadbalancingHTTPFrontendOutput {
	return o
}

type IPLoadbalancingHTTPFrontendArrayOutput struct{ *pulumi.OutputState }

func (IPLoadbalancingHTTPFrontendArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPLoadbalancingHTTPFrontend)(nil)).Elem()
}

func (o IPLoadbalancingHTTPFrontendArrayOutput) ToIPLoadbalancingHTTPFrontendArrayOutput() IPLoadbalancingHTTPFrontendArrayOutput {
	return o
}

func (o IPLoadbalancingHTTPFrontendArrayOutput) ToIPLoadbalancingHTTPFrontendArrayOutputWithContext(ctx context.Context) IPLoadbalancingHTTPFrontendArrayOutput {
	return o
}

func (o IPLoadbalancingHTTPFrontendArrayOutput) Index(i pulumi.IntInput) IPLoadbalancingHTTPFrontendOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *IPLoadbalancingHTTPFrontend {
		return vs[0].([]*IPLoadbalancingHTTPFrontend)[vs[1].(int)]
	}).(IPLoadbalancingHTTPFrontendOutput)
}

type IPLoadbalancingHTTPFrontendMapOutput struct{ *pulumi.OutputState }

func (IPLoadbalancingHTTPFrontendMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPLoadbalancingHTTPFrontend)(nil)).Elem()
}

func (o IPLoadbalancingHTTPFrontendMapOutput) ToIPLoadbalancingHTTPFrontendMapOutput() IPLoadbalancingHTTPFrontendMapOutput {
	return o
}

func (o IPLoadbalancingHTTPFrontendMapOutput) ToIPLoadbalancingHTTPFrontendMapOutputWithContext(ctx context.Context) IPLoadbalancingHTTPFrontendMapOutput {
	return o
}

func (o IPLoadbalancingHTTPFrontendMapOutput) MapIndex(k pulumi.StringInput) IPLoadbalancingHTTPFrontendOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *IPLoadbalancingHTTPFrontend {
		return vs[0].(map[string]*IPLoadbalancingHTTPFrontend)[vs[1].(string)]
	}).(IPLoadbalancingHTTPFrontendOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IPLoadbalancingHTTPFrontendInput)(nil)).Elem(), &IPLoadbalancingHTTPFrontend{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPLoadbalancingHTTPFrontendArrayInput)(nil)).Elem(), IPLoadbalancingHTTPFrontendArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPLoadbalancingHTTPFrontendMapInput)(nil)).Elem(), IPLoadbalancingHTTPFrontendMap{})
	pulumi.RegisterOutputType(IPLoadbalancingHTTPFrontendOutput{})
	pulumi.RegisterOutputType(IPLoadbalancingHTTPFrontendArrayOutput{})
	pulumi.RegisterOutputType(IPLoadbalancingHTTPFrontendMapOutput{})
}
