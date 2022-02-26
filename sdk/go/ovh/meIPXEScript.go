// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates an IPXE Script.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
// 	"io/ioutil"
//
// 	"github.com/pulumi/pulumi-ovh/sdk/go/ovh"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func readFileOrPanic(path string) pulumi.StringPtrInput {
// 	data, err := ioutil.ReadFile(path)
// 	if err != nil {
// 		panic(err.Error())
// 	}
// 	return pulumi.String(string(data))
// }
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ovh.NewMeIPXEScript(ctx, "script", &ovh.MeIPXEScriptArgs{
// 			Script: readFileOrPanic(fmt.Sprintf("%v%v", path.Module, "/boot.ipxe")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type MeIPXEScript struct {
	pulumi.CustomResourceState

	// For documentation purpose only. This attribute is not passed to the OVH API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
	Description pulumi.StringOutput `pulumi:"description"`
	// The name of the IPXE Script.
	Name pulumi.StringOutput `pulumi:"name"`
	// The content of the script.
	Script pulumi.StringOutput `pulumi:"script"`
}

// NewMeIPXEScript registers a new resource with the given unique name, arguments, and options.
func NewMeIPXEScript(ctx *pulumi.Context,
	name string, args *MeIPXEScriptArgs, opts ...pulumi.ResourceOption) (*MeIPXEScript, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Script == nil {
		return nil, errors.New("invalid value for required argument 'Script'")
	}
	var resource MeIPXEScript
	err := ctx.RegisterResource("ovh:index/meIPXEScript:MeIPXEScript", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMeIPXEScript gets an existing MeIPXEScript resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMeIPXEScript(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MeIPXEScriptState, opts ...pulumi.ResourceOption) (*MeIPXEScript, error) {
	var resource MeIPXEScript
	err := ctx.ReadResource("ovh:index/meIPXEScript:MeIPXEScript", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MeIPXEScript resources.
type meIPXEScriptState struct {
	// For documentation purpose only. This attribute is not passed to the OVH API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
	Description *string `pulumi:"description"`
	// The name of the IPXE Script.
	Name *string `pulumi:"name"`
	// The content of the script.
	Script *string `pulumi:"script"`
}

type MeIPXEScriptState struct {
	// For documentation purpose only. This attribute is not passed to the OVH API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
	Description pulumi.StringPtrInput
	// The name of the IPXE Script.
	Name pulumi.StringPtrInput
	// The content of the script.
	Script pulumi.StringPtrInput
}

func (MeIPXEScriptState) ElementType() reflect.Type {
	return reflect.TypeOf((*meIPXEScriptState)(nil)).Elem()
}

type meIPXEScriptArgs struct {
	// For documentation purpose only. This attribute is not passed to the OVH API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
	Description *string `pulumi:"description"`
	// The name of the IPXE Script.
	Name *string `pulumi:"name"`
	// The content of the script.
	Script string `pulumi:"script"`
}

// The set of arguments for constructing a MeIPXEScript resource.
type MeIPXEScriptArgs struct {
	// For documentation purpose only. This attribute is not passed to the OVH API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
	Description pulumi.StringPtrInput
	// The name of the IPXE Script.
	Name pulumi.StringPtrInput
	// The content of the script.
	Script pulumi.StringInput
}

func (MeIPXEScriptArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*meIPXEScriptArgs)(nil)).Elem()
}

type MeIPXEScriptInput interface {
	pulumi.Input

	ToMeIPXEScriptOutput() MeIPXEScriptOutput
	ToMeIPXEScriptOutputWithContext(ctx context.Context) MeIPXEScriptOutput
}

func (*MeIPXEScript) ElementType() reflect.Type {
	return reflect.TypeOf((**MeIPXEScript)(nil)).Elem()
}

func (i *MeIPXEScript) ToMeIPXEScriptOutput() MeIPXEScriptOutput {
	return i.ToMeIPXEScriptOutputWithContext(context.Background())
}

func (i *MeIPXEScript) ToMeIPXEScriptOutputWithContext(ctx context.Context) MeIPXEScriptOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MeIPXEScriptOutput)
}

// MeIPXEScriptArrayInput is an input type that accepts MeIPXEScriptArray and MeIPXEScriptArrayOutput values.
// You can construct a concrete instance of `MeIPXEScriptArrayInput` via:
//
//          MeIPXEScriptArray{ MeIPXEScriptArgs{...} }
type MeIPXEScriptArrayInput interface {
	pulumi.Input

	ToMeIPXEScriptArrayOutput() MeIPXEScriptArrayOutput
	ToMeIPXEScriptArrayOutputWithContext(context.Context) MeIPXEScriptArrayOutput
}

type MeIPXEScriptArray []MeIPXEScriptInput

func (MeIPXEScriptArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*MeIPXEScript)(nil)).Elem()
}

func (i MeIPXEScriptArray) ToMeIPXEScriptArrayOutput() MeIPXEScriptArrayOutput {
	return i.ToMeIPXEScriptArrayOutputWithContext(context.Background())
}

func (i MeIPXEScriptArray) ToMeIPXEScriptArrayOutputWithContext(ctx context.Context) MeIPXEScriptArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MeIPXEScriptArrayOutput)
}

// MeIPXEScriptMapInput is an input type that accepts MeIPXEScriptMap and MeIPXEScriptMapOutput values.
// You can construct a concrete instance of `MeIPXEScriptMapInput` via:
//
//          MeIPXEScriptMap{ "key": MeIPXEScriptArgs{...} }
type MeIPXEScriptMapInput interface {
	pulumi.Input

	ToMeIPXEScriptMapOutput() MeIPXEScriptMapOutput
	ToMeIPXEScriptMapOutputWithContext(context.Context) MeIPXEScriptMapOutput
}

type MeIPXEScriptMap map[string]MeIPXEScriptInput

func (MeIPXEScriptMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*MeIPXEScript)(nil)).Elem()
}

func (i MeIPXEScriptMap) ToMeIPXEScriptMapOutput() MeIPXEScriptMapOutput {
	return i.ToMeIPXEScriptMapOutputWithContext(context.Background())
}

func (i MeIPXEScriptMap) ToMeIPXEScriptMapOutputWithContext(ctx context.Context) MeIPXEScriptMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MeIPXEScriptMapOutput)
}

type MeIPXEScriptOutput struct{ *pulumi.OutputState }

func (MeIPXEScriptOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MeIPXEScript)(nil)).Elem()
}

func (o MeIPXEScriptOutput) ToMeIPXEScriptOutput() MeIPXEScriptOutput {
	return o
}

func (o MeIPXEScriptOutput) ToMeIPXEScriptOutputWithContext(ctx context.Context) MeIPXEScriptOutput {
	return o
}

type MeIPXEScriptArrayOutput struct{ *pulumi.OutputState }

func (MeIPXEScriptArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*MeIPXEScript)(nil)).Elem()
}

func (o MeIPXEScriptArrayOutput) ToMeIPXEScriptArrayOutput() MeIPXEScriptArrayOutput {
	return o
}

func (o MeIPXEScriptArrayOutput) ToMeIPXEScriptArrayOutputWithContext(ctx context.Context) MeIPXEScriptArrayOutput {
	return o
}

func (o MeIPXEScriptArrayOutput) Index(i pulumi.IntInput) MeIPXEScriptOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *MeIPXEScript {
		return vs[0].([]*MeIPXEScript)[vs[1].(int)]
	}).(MeIPXEScriptOutput)
}

type MeIPXEScriptMapOutput struct{ *pulumi.OutputState }

func (MeIPXEScriptMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*MeIPXEScript)(nil)).Elem()
}

func (o MeIPXEScriptMapOutput) ToMeIPXEScriptMapOutput() MeIPXEScriptMapOutput {
	return o
}

func (o MeIPXEScriptMapOutput) ToMeIPXEScriptMapOutputWithContext(ctx context.Context) MeIPXEScriptMapOutput {
	return o
}

func (o MeIPXEScriptMapOutput) MapIndex(k pulumi.StringInput) MeIPXEScriptOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *MeIPXEScript {
		return vs[0].(map[string]*MeIPXEScript)[vs[1].(string)]
	}).(MeIPXEScriptOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MeIPXEScriptInput)(nil)).Elem(), &MeIPXEScript{})
	pulumi.RegisterInputType(reflect.TypeOf((*MeIPXEScriptArrayInput)(nil)).Elem(), MeIPXEScriptArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*MeIPXEScriptMapInput)(nil)).Elem(), MeIPXEScriptMap{})
	pulumi.RegisterOutputType(MeIPXEScriptOutput{})
	pulumi.RegisterOutputType(MeIPXEScriptArrayOutput{})
	pulumi.RegisterOutputType(MeIPXEScriptMapOutput{})
}