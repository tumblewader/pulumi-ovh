// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get the list of compatible netboots for a dedicated server associated with your OVH Account.
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
// 		_, err := ovh.GetDedicatedServerBoots(ctx, &GetDedicatedServerBootsArgs{
// 			BootType:    pulumi.StringRef("harddisk"),
// 			ServiceName: "myserver",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetDedicatedServerBoots(ctx *pulumi.Context, args *GetDedicatedServerBootsArgs, opts ...pulumi.InvokeOption) (*GetDedicatedServerBootsResult, error) {
	var rv GetDedicatedServerBootsResult
	err := ctx.Invoke("ovh:index/getDedicatedServerBoots:getDedicatedServerBoots", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDedicatedServerBoots.
type GetDedicatedServerBootsArgs struct {
	// Filter the value of bootType property (harddisk, rescue, ipxeCustomerScript, internal, network)
	BootType *string `pulumi:"bootType"`
	Kernel   *string `pulumi:"kernel"`
	// The internal name of your dedicated server.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getDedicatedServerBoots.
type GetDedicatedServerBootsResult struct {
	BootType *string `pulumi:"bootType"`
	// The provider-assigned unique ID for this managed resource.
	Id     string  `pulumi:"id"`
	Kernel *string `pulumi:"kernel"`
	// The list of dedicated server netboots.
	Results     []int  `pulumi:"results"`
	ServiceName string `pulumi:"serviceName"`
}

func GetDedicatedServerBootsOutput(ctx *pulumi.Context, args GetDedicatedServerBootsOutputArgs, opts ...pulumi.InvokeOption) GetDedicatedServerBootsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetDedicatedServerBootsResult, error) {
			args := v.(GetDedicatedServerBootsArgs)
			r, err := GetDedicatedServerBoots(ctx, &args, opts...)
			return *r, err
		}).(GetDedicatedServerBootsResultOutput)
}

// A collection of arguments for invoking getDedicatedServerBoots.
type GetDedicatedServerBootsOutputArgs struct {
	// Filter the value of bootType property (harddisk, rescue, ipxeCustomerScript, internal, network)
	BootType pulumi.StringPtrInput `pulumi:"bootType"`
	Kernel   pulumi.StringPtrInput `pulumi:"kernel"`
	// The internal name of your dedicated server.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (GetDedicatedServerBootsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDedicatedServerBootsArgs)(nil)).Elem()
}

// A collection of values returned by getDedicatedServerBoots.
type GetDedicatedServerBootsResultOutput struct{ *pulumi.OutputState }

func (GetDedicatedServerBootsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDedicatedServerBootsResult)(nil)).Elem()
}

func (o GetDedicatedServerBootsResultOutput) ToGetDedicatedServerBootsResultOutput() GetDedicatedServerBootsResultOutput {
	return o
}

func (o GetDedicatedServerBootsResultOutput) ToGetDedicatedServerBootsResultOutputWithContext(ctx context.Context) GetDedicatedServerBootsResultOutput {
	return o
}

func (o GetDedicatedServerBootsResultOutput) BootType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetDedicatedServerBootsResult) *string { return v.BootType }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetDedicatedServerBootsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetDedicatedServerBootsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetDedicatedServerBootsResultOutput) Kernel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetDedicatedServerBootsResult) *string { return v.Kernel }).(pulumi.StringPtrOutput)
}

// The list of dedicated server netboots.
func (o GetDedicatedServerBootsResultOutput) Results() pulumi.IntArrayOutput {
	return o.ApplyT(func(v GetDedicatedServerBootsResult) []int { return v.Results }).(pulumi.IntArrayOutput)
}

func (o GetDedicatedServerBootsResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetDedicatedServerBootsResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetDedicatedServerBootsResultOutput{})
}
