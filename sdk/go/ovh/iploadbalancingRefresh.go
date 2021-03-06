// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Applies changes from other ovh_iploadbalancing_* resourcesto the production configuration of loadbalancers.
type IPLoadbalancingRefresh struct {
	pulumi.CustomResourceState

	// List of values traccked to trigger refresh, used also to form implicit dependencies
	Keepers pulumi.StringArrayOutput `pulumi:"keepers"`
	// The internal name of your IP load balancing
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
}

// NewIPLoadbalancingRefresh registers a new resource with the given unique name, arguments, and options.
func NewIPLoadbalancingRefresh(ctx *pulumi.Context,
	name string, args *IPLoadbalancingRefreshArgs, opts ...pulumi.ResourceOption) (*IPLoadbalancingRefresh, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Keepers == nil {
		return nil, errors.New("invalid value for required argument 'Keepers'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	var resource IPLoadbalancingRefresh
	err := ctx.RegisterResource("ovh:index/iPLoadbalancingRefresh:IPLoadbalancingRefresh", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIPLoadbalancingRefresh gets an existing IPLoadbalancingRefresh resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIPLoadbalancingRefresh(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IPLoadbalancingRefreshState, opts ...pulumi.ResourceOption) (*IPLoadbalancingRefresh, error) {
	var resource IPLoadbalancingRefresh
	err := ctx.ReadResource("ovh:index/iPLoadbalancingRefresh:IPLoadbalancingRefresh", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IPLoadbalancingRefresh resources.
type iploadbalancingRefreshState struct {
	// List of values traccked to trigger refresh, used also to form implicit dependencies
	Keepers []string `pulumi:"keepers"`
	// The internal name of your IP load balancing
	ServiceName *string `pulumi:"serviceName"`
}

type IPLoadbalancingRefreshState struct {
	// List of values traccked to trigger refresh, used also to form implicit dependencies
	Keepers pulumi.StringArrayInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringPtrInput
}

func (IPLoadbalancingRefreshState) ElementType() reflect.Type {
	return reflect.TypeOf((*iploadbalancingRefreshState)(nil)).Elem()
}

type iploadbalancingRefreshArgs struct {
	// List of values traccked to trigger refresh, used also to form implicit dependencies
	Keepers []string `pulumi:"keepers"`
	// The internal name of your IP load balancing
	ServiceName string `pulumi:"serviceName"`
}

// The set of arguments for constructing a IPLoadbalancingRefresh resource.
type IPLoadbalancingRefreshArgs struct {
	// List of values traccked to trigger refresh, used also to form implicit dependencies
	Keepers pulumi.StringArrayInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringInput
}

func (IPLoadbalancingRefreshArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*iploadbalancingRefreshArgs)(nil)).Elem()
}

type IPLoadbalancingRefreshInput interface {
	pulumi.Input

	ToIPLoadbalancingRefreshOutput() IPLoadbalancingRefreshOutput
	ToIPLoadbalancingRefreshOutputWithContext(ctx context.Context) IPLoadbalancingRefreshOutput
}

func (*IPLoadbalancingRefresh) ElementType() reflect.Type {
	return reflect.TypeOf((**IPLoadbalancingRefresh)(nil)).Elem()
}

func (i *IPLoadbalancingRefresh) ToIPLoadbalancingRefreshOutput() IPLoadbalancingRefreshOutput {
	return i.ToIPLoadbalancingRefreshOutputWithContext(context.Background())
}

func (i *IPLoadbalancingRefresh) ToIPLoadbalancingRefreshOutputWithContext(ctx context.Context) IPLoadbalancingRefreshOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPLoadbalancingRefreshOutput)
}

// IPLoadbalancingRefreshArrayInput is an input type that accepts IPLoadbalancingRefreshArray and IPLoadbalancingRefreshArrayOutput values.
// You can construct a concrete instance of `IPLoadbalancingRefreshArrayInput` via:
//
//          IPLoadbalancingRefreshArray{ IPLoadbalancingRefreshArgs{...} }
type IPLoadbalancingRefreshArrayInput interface {
	pulumi.Input

	ToIPLoadbalancingRefreshArrayOutput() IPLoadbalancingRefreshArrayOutput
	ToIPLoadbalancingRefreshArrayOutputWithContext(context.Context) IPLoadbalancingRefreshArrayOutput
}

type IPLoadbalancingRefreshArray []IPLoadbalancingRefreshInput

func (IPLoadbalancingRefreshArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPLoadbalancingRefresh)(nil)).Elem()
}

func (i IPLoadbalancingRefreshArray) ToIPLoadbalancingRefreshArrayOutput() IPLoadbalancingRefreshArrayOutput {
	return i.ToIPLoadbalancingRefreshArrayOutputWithContext(context.Background())
}

func (i IPLoadbalancingRefreshArray) ToIPLoadbalancingRefreshArrayOutputWithContext(ctx context.Context) IPLoadbalancingRefreshArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPLoadbalancingRefreshArrayOutput)
}

// IPLoadbalancingRefreshMapInput is an input type that accepts IPLoadbalancingRefreshMap and IPLoadbalancingRefreshMapOutput values.
// You can construct a concrete instance of `IPLoadbalancingRefreshMapInput` via:
//
//          IPLoadbalancingRefreshMap{ "key": IPLoadbalancingRefreshArgs{...} }
type IPLoadbalancingRefreshMapInput interface {
	pulumi.Input

	ToIPLoadbalancingRefreshMapOutput() IPLoadbalancingRefreshMapOutput
	ToIPLoadbalancingRefreshMapOutputWithContext(context.Context) IPLoadbalancingRefreshMapOutput
}

type IPLoadbalancingRefreshMap map[string]IPLoadbalancingRefreshInput

func (IPLoadbalancingRefreshMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPLoadbalancingRefresh)(nil)).Elem()
}

func (i IPLoadbalancingRefreshMap) ToIPLoadbalancingRefreshMapOutput() IPLoadbalancingRefreshMapOutput {
	return i.ToIPLoadbalancingRefreshMapOutputWithContext(context.Background())
}

func (i IPLoadbalancingRefreshMap) ToIPLoadbalancingRefreshMapOutputWithContext(ctx context.Context) IPLoadbalancingRefreshMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPLoadbalancingRefreshMapOutput)
}

type IPLoadbalancingRefreshOutput struct{ *pulumi.OutputState }

func (IPLoadbalancingRefreshOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IPLoadbalancingRefresh)(nil)).Elem()
}

func (o IPLoadbalancingRefreshOutput) ToIPLoadbalancingRefreshOutput() IPLoadbalancingRefreshOutput {
	return o
}

func (o IPLoadbalancingRefreshOutput) ToIPLoadbalancingRefreshOutputWithContext(ctx context.Context) IPLoadbalancingRefreshOutput {
	return o
}

type IPLoadbalancingRefreshArrayOutput struct{ *pulumi.OutputState }

func (IPLoadbalancingRefreshArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPLoadbalancingRefresh)(nil)).Elem()
}

func (o IPLoadbalancingRefreshArrayOutput) ToIPLoadbalancingRefreshArrayOutput() IPLoadbalancingRefreshArrayOutput {
	return o
}

func (o IPLoadbalancingRefreshArrayOutput) ToIPLoadbalancingRefreshArrayOutputWithContext(ctx context.Context) IPLoadbalancingRefreshArrayOutput {
	return o
}

func (o IPLoadbalancingRefreshArrayOutput) Index(i pulumi.IntInput) IPLoadbalancingRefreshOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *IPLoadbalancingRefresh {
		return vs[0].([]*IPLoadbalancingRefresh)[vs[1].(int)]
	}).(IPLoadbalancingRefreshOutput)
}

type IPLoadbalancingRefreshMapOutput struct{ *pulumi.OutputState }

func (IPLoadbalancingRefreshMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPLoadbalancingRefresh)(nil)).Elem()
}

func (o IPLoadbalancingRefreshMapOutput) ToIPLoadbalancingRefreshMapOutput() IPLoadbalancingRefreshMapOutput {
	return o
}

func (o IPLoadbalancingRefreshMapOutput) ToIPLoadbalancingRefreshMapOutputWithContext(ctx context.Context) IPLoadbalancingRefreshMapOutput {
	return o
}

func (o IPLoadbalancingRefreshMapOutput) MapIndex(k pulumi.StringInput) IPLoadbalancingRefreshOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *IPLoadbalancingRefresh {
		return vs[0].(map[string]*IPLoadbalancingRefresh)[vs[1].(string)]
	}).(IPLoadbalancingRefreshOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IPLoadbalancingRefreshInput)(nil)).Elem(), &IPLoadbalancingRefresh{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPLoadbalancingRefreshArrayInput)(nil)).Elem(), IPLoadbalancingRefreshArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPLoadbalancingRefreshMapInput)(nil)).Elem(), IPLoadbalancingRefreshMap{})
	pulumi.RegisterOutputType(IPLoadbalancingRefreshOutput{})
	pulumi.RegisterOutputType(IPLoadbalancingRefreshArrayOutput{})
	pulumi.RegisterOutputType(IPLoadbalancingRefreshMapOutput{})
}
